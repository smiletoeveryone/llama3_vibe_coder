# Very basic syntax check placeholder

def verify_code_style(code: str, lang: str = "py") -> str:
    if lang == "py" and not code.strip().startswith("def") and "import" not in code:
        return "# Warning: Code might not be valid Python\n" + code
    return code
