from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/text_response")
async def text_response(request: Request):
    return PlainTextResponse("This is a plain text response from your                                   FastAPI backend.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
