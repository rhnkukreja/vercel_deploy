from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/voice")
async def voice(request: Request):
    base_url = str(request.url)
    handle_call_url = urljoin(base_url, '/handle_call')
    response = f"""
    <Response>
        <Say>Welcome to your personal AI assistant.</Say>
        <Say>Please wait while I connect you to the AI assistant.</Say>
        <Redirect>{handle_call_url}</Redirect>
    </Response>
    """
    return PlainTextResponse(response, media_type="application/xml")

@app.post("/handle_call")
async def handle_call(request: Request):
    # Here you integrate your AI bot logic
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
