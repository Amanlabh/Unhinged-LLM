#!/bin/bash
# Start FastAPI server for Cyber Fellow

echo "🛡️  Starting Cyber Fellow API Server..."
echo ""

# Check if Ollama is running
if ! curl -s http://localhost:11434 > /dev/null 2>&1; then
    echo "⚠️  Warning: Ollama doesn't seem to be running."
    echo "Please make sure Ollama is running: ollama serve"
    echo ""
fi

# Check if Python dependencies are installed
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "📦 Installing Python dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Start the FastAPI server
echo "🚀 Starting server on http://localhost:8000"
echo "📚 API docs available at http://localhost:8000/docs"
echo ""
python3 -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000




