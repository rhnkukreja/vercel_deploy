from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/voice")
async def voice(request: Request):
    response = """
    <Response>
        <Say>Welcome to your personal AI assistant.</Say>
        <Say>Please wait while I connect you to the AI assistant.</Say>
        <Redirect>https://<your-vercel-app>.vercel.app/handle_call</Redirect>
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
