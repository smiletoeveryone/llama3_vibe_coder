# Load Ollama LLaMA 3.3 model
import requests
from config.model_config import MODEL_NAME

def generate_response(prompt: str, stream: bool = False):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": stream
    })
    return response.json()["response"]
