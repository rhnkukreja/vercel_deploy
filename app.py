from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/text_response")
async def text_response(request: Request):
    return PlainTextResponse("""Hello, how can i assist you today?                            
                                What type of room would you like, we have standard and executive room type                                                                                    
                                Yes, we do. The price is 4000 per night.                                                                                    
                                Anything else i can help you with?                                                                                    
                                Have a Good day
                                """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
