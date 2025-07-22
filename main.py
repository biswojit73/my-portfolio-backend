from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from groq_api import get_groq_response

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class VoiceRequest(BaseModel):
    text: str

# ✅ API route
@app.post("/api/voice")
async def voice_control(request: VoiceRequest):
    if not request.text:
        return JSONResponse(status_code=400, content={"error": "Text is required"})

    # Call your AI function
    ai_response = get_groq_response(request.text)

    return {
        "message": f"You said: {request.text}",
        "response": ai_response
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

