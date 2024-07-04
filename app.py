import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import Response
from twilio.rest import Client
import requests
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()




app = FastAPI()

# Set environment variables for your credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

@app.post("/voice_org")
async def voice(request: Request):
    """Respond to incoming requests with a TwiML message"""
    resp = """
    <Response>
        <Say>Please leave a message after the beep. Press the star key when finished.</Say>
        <Record action="/handle-recording" method="POST" maxLength="20" finishOnKey="*"/>
        <Say>We didn't receive any input. Goodbye!</Say>
    </Response>
    """
    return Response(content=resp, media_type="application/xml")

@app.get("/voice")
async def voice(request: Request):
    """Respond to incoming requests with a TwiML message"""
    resp = """
    <Response>
        <Say>Please leave a message after the beep. Press the star key when finished. Now the hell to do with this man ?</Say>
    </Response>
    """
    return Response(content=resp, media_type="application/xml")


@app.post("/handle-recording")
async def handle_recording(RecordingUrl: str = Form(...)):
    """Handle the recording and process the text"""
    # Process the recorded text (example function call)
    await process_recording(RecordingUrl)
    return "Recording received, thank you!"

async def process_recording(recording_url: str):
    # Example function to download and process the recording
    recording = requests.get(recording_url)
    # Here you can add your speech-to-text processing code
    print(f"Recording URL: {recording_url}")
    # Placeholder for your speech-to-text function
    recorded_text = "This is a dummy text from the recording."
    await handle_recorded_text(recorded_text)

async def handle_recorded_text(text: str):
    # Handle the transcribed text from the recording
    print(f"Recorded text: {text}")
    # Further processing can be done here

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI on Vercel!"}

