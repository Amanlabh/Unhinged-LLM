"""Ollama client for interacting with local LLM"""
import ollama
from typing import Optional, Iterator
from config import OLLAMA_BASE_URL, DEFAULT_MODEL, USE_GENERATE
from cyber_knowledge import get_cyber_context

class OllamaClient:
    """Client for interacting with Ollama API"""
    
    def __init__(self, model: Optional[str] = None, base_url: Optional[str] = None, use_generate: Optional[bool] = None):
        self.model = model or DEFAULT_MODEL
        self.base_url = base_url or OLLAMA_BASE_URL
        self.client = ollama.Client(host=self.base_url)
        self.system_prompt = get_cyber_context()
        # Use generate() instead of chat() for less restrictions
        self.use_generate = use_generate if use_generate is not None else USE_GENERATE
    
    def check_connection(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            self.client.list()
            return True
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            print(f"Make sure Ollama is running at {self.base_url}")
            return False
    
    def list_models(self) -> list:
        """List available models"""
        try:
            response = self.client.list()
            # Handle different response formats
            if isinstance(response, dict) and 'models' in response:
                return [model.get('name', model.get('model', '')) for model in response['models']]
            elif isinstance(response, list):
                return [model.get('name', model.get('model', '')) for model in response]
            else:
                return []
        except Exception as e:
            print(f"Error listing models: {e}")
            return []
    
    def chat(self, message: str, stream: bool = True, history: Optional[list] = None) -> Iterator[str]:
        """Send a message to the AI and get response"""
        # Use generate() if configured, as it sometimes bypasses restrictions better
        if self.use_generate:
            yield from self.generate(message, stream)
            return
        
        # Build messages list with system prompt and history
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history if provided
        if history:
            messages.extend(history)
        
        # Add current user message
        messages.append({"role": "user", "content": message})
            
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                stream=stream,
                options={
                    "temperature": 1.0,  # Higher creativity
                    "top_p": 0.9,       # Nucleus sampling
                    "num_predict": -1,   # No limit on response length
                }
            )
            
            if stream:
                for chunk in response:
                    if 'message' in chunk and 'content' in chunk['message']:
                        yield chunk['message']['content']
            else:
                if 'message' in response and 'content' in response['message']:
                    yield response['message']['content']
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def generate(self, prompt: str, stream: bool = True) -> Iterator[str]:
        """Generate text from a prompt"""
        try:
            full_prompt = f"{self.system_prompt}\n\nUser: {prompt}\n\nAssistant:"
            response = self.client.generate(
                model=self.model,
                prompt=full_prompt,
                stream=stream,
                options={
                    "temperature": 1.0,
                    "top_p": 0.9,
                    "num_predict": -1,
                }
            )
            
            if stream:
                for chunk in response:
                    if 'response' in chunk:
                        yield chunk['response']
            else:
                if 'response' in response:
                    yield response['response']
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def set_model(self, model: str):
        """Change the model being used"""
        self.model = model
        print(f"Switched to model: {model}")

