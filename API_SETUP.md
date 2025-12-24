# FastAPI Backend Setup

## Overview

The FastAPI backend serves the Python Cyber Fellow assistant, providing:
- Cybersecurity knowledge base integration
- Ollama connection management
- Streaming chat responses
- RESTful API endpoints

## Setup

### 1. Install Dependencies

```bash
cd cyber-fellow
pip install -r requirements.txt
```

This installs:
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)
- All existing dependencies

### 2. Start the FastAPI Server

```bash
./start_api.sh
```

Or manually:
```bash
python3 -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`

### 3. Configure Frontend

Make sure your Next.js app has the FastAPI URL in `.env.local`:

```env
FASTAPI_URL=http://localhost:8000
```

If not set, it defaults to `http://localhost:8000`

## API Endpoints

### Health Check
```
GET /health
```
Returns server and Ollama connection status.

### Chat (Non-streaming)
```
POST /api/chat
Body: {
  "message": "your message",
  "history": [{"role": "user", "content": "..."}, ...]
}
```

### Chat (Streaming) - Used by Frontend
```
POST /api/chat/stream
Body: {
  "message": "your message",
  "history": [{"role": "user", "content": "..."}, ...]
}
```
Returns Server-Sent Events (SSE) stream.

### List Models
```
GET /api/models
```
Returns available Ollama models.

### Change Model
```
POST /api/models/{model_name}
```
Changes the active model.

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Architecture

```
Next.js Frontend (port 3000)
    ↓
Next.js API Routes (/api/chat)
    ↓
FastAPI Backend (port 8000)
    ↓
Ollama (port 11434)
```

## Benefits

1. **Centralized Logic**: All cybersecurity knowledge and prompts in Python
2. **Better Error Handling**: Python-side validation and error management
3. **Scalability**: Can add more features (caching, rate limiting, etc.)
4. **Separation of Concerns**: Frontend handles UI, backend handles AI logic
5. **Reusability**: API can be used by other clients (mobile apps, CLI, etc.)

## Troubleshooting

### Port Already in Use
```bash
# Change port in start_api.sh or use:
uvicorn api.main:app --reload --port 8001
```

### Ollama Not Connected
- Make sure `ollama serve` is running
- Check `http://localhost:11434` is accessible
- Verify model exists: `ollama list`

### CORS Errors
- Check `allow_origins` in `api/main.py` includes your frontend URL
- For production, add your domain to CORS origins

## Production Deployment

For production:
1. Use a production ASGI server (Gunicorn + Uvicorn workers)
2. Set up reverse proxy (Nginx)
3. Configure environment variables
4. Set up SSL/TLS
5. Add authentication/rate limiting

Example with Gunicorn:
```bash
gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```


