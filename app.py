from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import time

app = FastAPI()

@app.get("/step1")
async def step1():
    response = """
Hello,....................................... how can I assist you today?
"""
    return PlainTextResponse(response, media_type="text/plain")

@app.get("/step2")
async def step2():
    response = """
What type of room would you like? We have standard and executive room types.
"""
    return PlainTextResponse(response, media_type="text/plain")

@app.get("/step3")
async def step3():
    response = """
Yes, we do. The price is 4000 per night.
"""
    return PlainTextResponse(response, media_type="text/plain")

@app.get("/step4")
async def step4():
    response = """
Anything else I can help you with?
"""
    return PlainTextResponse(response, media_type="text/plain")

@app.get("/step5")
async def step5():
    response = """
Have a good day!
"""
    return PlainTextResponse(response, media_type="text/plain")

@app.get("/passthru")
async def passthru():
    time.sleep(5)  # Simulate a pause by sleeping for 5 seconds
    response="  this is a pause"
    return PlainTextResponse(response, media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
