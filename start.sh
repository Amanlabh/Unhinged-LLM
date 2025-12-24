#!/bin/bash
# Quick start script for Cyber Fellow

echo "🛡️  Starting Cyber Fellow..."
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed!"
    echo "Please install Ollama from https://ollama.ai"
    exit 1
fi

# Check if Ollama is running
if ! curl -s http://localhost:11434 > /dev/null 2>&1; then
    echo "⚠️  Ollama doesn't seem to be running. Starting it..."
    echo "Please run 'ollama serve' in another terminal, or start Ollama manually."
    echo ""
fi

# Check if Python dependencies are installed
if ! python3 -c "import ollama" 2>/dev/null; then
    echo "📦 Installing Python dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Run the assistant
python3 main.py





