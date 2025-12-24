"""FastAPI server for Cyber Fellow"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import json
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ollama_client import OllamaClient
from cyber_knowledge import get_cyber_context

app = FastAPI(title="Unrestricted AI API", version="1.0.0")

# CORS middleware to allow Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Ollama client
ollama_client = OllamaClient()

# Request/Response models
class ChatMessage(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class HealthResponse(BaseModel):
    status: str
    model: str
    ollama_connected: bool

@app.get("/")
async def root():
    return {
        "message": "Unrestricted AI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "chat": "/api/chat",
            "stream": "/api/chat/stream"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check API and Ollama connection status"""
    is_connected = ollama_client.check_connection()
    return HealthResponse(
        status="healthy" if is_connected else "unhealthy",
        model=ollama_client.model,
        ollama_connected=is_connected
    )

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Non-streaming chat endpoint"""
    if not ollama_client.check_connection():
        raise HTTPException(status_code=503, detail="Ollama is not connected")
    
    # Convert history to format expected by Ollama
    conversation_history = []
    for msg in request.history:
        conversation_history.append({
            "role": msg.role,
            "content": msg.content
        })
    
    # Get response from Ollama
    full_response = ""
    try:
        for chunk in ollama_client.chat(request.message, stream=False, history=conversation_history):
            full_response += chunk
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting response: {str(e)}")
    
    return {
        "response": full_response,
        "model": ollama_client.model
    }

@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    """Streaming chat endpoint for real-time responses"""
    if not ollama_client.check_connection():
        raise HTTPException(status_code=503, detail="Ollama is not connected")
    
    # Convert history to format expected by Ollama
    conversation_history = []
    for msg in request.history:
        conversation_history.append({
            "role": msg.role,
            "content": msg.content
        })
    
    def generate():
        try:
            for chunk in ollama_client.chat(request.message, stream=True, history=conversation_history):
                if chunk:
                    # Format as Server-Sent Events (SSE)
                    data = json.dumps({"content": chunk})
                    yield f"data: {data}\n\n"
            # Send done signal
            yield "data: [DONE]\n\n"
        except Exception as e:
            error_data = json.dumps({"error": str(e)})
            yield f"data: {error_data}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

@app.get("/api/models")
async def list_models():
    """List available Ollama models"""
    models = ollama_client.list_models()
    return {"models": models}

@app.post("/api/models/{model_name}")
async def set_model(model_name: str):
    """Change the active model"""
    ollama_client.set_model(model_name)
    return {"message": f"Model changed to {model_name}", "model": ollama_client.model}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

