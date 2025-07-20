# Clean up or validate user prompts for safety

def filter_prompt(prompt: str) -> str:
    blocked_keywords = ["rm -rf", "delete system32"]
    for word in blocked_keywords:
        prompt = prompt.replace(word, "[BLOCKED]")
    return prompt
