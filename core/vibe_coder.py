# VibeCoder AI - Code-centric logic and refactor suggestions
from core.model_loader import generate_response
from utils.syntax_checker import verify_code_style
from utils.cache_manager import store_session, get_session_history

def generate_code(user_prompt: str, lang: str = "py") -> str:
    history = get_session_history()
    full_prompt = f"{history}\nUser: {user_prompt} [Language: {lang}]\nAI:"
    response = generate_response(full_prompt)
    store_session(user_prompt, response)
    return verify_code_style(response, lang)
