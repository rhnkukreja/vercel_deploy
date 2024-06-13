from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/handle_audio")
async def handle_audio(request: Request):
    logging.info("Received audio for processing")
    # Simulate processing
    ai_response = "This is your AI assistant speaking."
    response = f"""
    <Response>
        <Say>{ai_response}</Say>
    </Response>
    """
    return PlainTextResponse(response, media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
