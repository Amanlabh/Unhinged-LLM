"""Configuration settings for Cyber Fellow"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

# Ollama settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
# Note: For unrestricted responses, consider using uncensored models like:
# "llama3.2", "mistral", "codellama", or community uncensored variants
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
# Use generate() instead of chat() - sometimes bypasses restrictions better
USE_GENERATE = os.getenv("USE_GENERATE", "false").lower() == "true"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
KNOWLEDGE_DIR.mkdir(exist_ok=True)

