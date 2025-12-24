#!/bin/bash
# Script to help free up space for mistral model

echo "Current Ollama models:"
ollama list

echo ""
echo "To free up space, you can remove old models:"
echo ""
echo "Remove llama2:7b (3.8 GB):"
echo "  ollama rm llama2:7b"
echo ""
echo "Remove llama3.2:1b (1.3 GB) if you don't need it:"
echo "  ollama rm llama3.2:1b"
echo ""
echo "Remove gpt-oss:120b-cloud if you don't need it:"
echo "  ollama rm gpt-oss:120b-cloud"
echo ""
echo "After freeing space, pull mistral:"
echo "  ollama pull mistral"
echo ""
echo "Or use the model you already have (llama3.2:latest) which works great!"



