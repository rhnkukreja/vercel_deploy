from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from urllib.parse import urljoin
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.get("/voice")
async def voice(request: Request):
    logging.info(f"Received /voice request with headers: {request.headers} and body: {request.query_params}")
    response = """
    <Response>
        <Say>Welcome to your personal AI assistant.</Say>
        <Say>Please wait while I connect you to the AI assistant.</Say>
    </Response>
    """
    logging.info(f"Responding with TwiML for /voice: {response}")
    return PlainTextResponse(response, media_type="application/xml")

@app.get("/handle_call")
async def handle_call(request: Request):
    logging.info(f"Received /handle_call request with headers: {request.headers} and body: {request.query_params}")
    # Here you integrate your AI bot logic
    ai_response = "This is your AI assistant speaking."
    response = f"""
    <Response>
        <Say>{ai_response}</Say>
    </Response>
    """
    logging.info(f"Responding with TwiML for /handle_call: {response}")
    return PlainTextResponse(response, media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
