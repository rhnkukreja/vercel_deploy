from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/handle_audio")
async def handle_audio(request: Request):
    logging.info("Received request for handle_audio")
    response = """
    <Response>
        <Gather action="https://your-backend-url.com/handle_input" method="POST" numDigits="1" timeout="5">
            <Say>Please enter a digit.</Say>
        </Gather>
        <Say>We didn't receive any input. Goodbye!</Say>
    </Response>
    """
    return PlainTextResponse(response, media_type="application/xml")

@app.post("/handle_input")
async def handle_input(request: Request):
    # Process the gathered input
    form_data = await request.form()
    digits = form_data.get("Digits")
    logging.info(f"Received digits: {digits}")
    
    response_text = "You entered: " + (digits if digits else "nothing")
    response = f"""
    <Response>
        <Say>{response_text}</Say>
    </Response>
    """
    return PlainTextResponse(response, media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
