# Manage code prompt history for context continuity
_code_memory = []

def store_session(prompt: str, code: str):
    _code_memory.append((prompt, code))
    if len(_code_memory) > 10:
        _code_memory.pop(0)

def get_session_history():
    return "\n".join([f"User: {p}\nAI: {c}" for p, c in _code_memory])

def get_memory_list():
    return list(_code_memory)
