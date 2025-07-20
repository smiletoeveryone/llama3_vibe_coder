# CLI for Vibe Coding Assistant with chat history and typewriter effect
from core.vibe_coder import generate_code
from data.dataset_filter import filter_prompt
from core.tools import save_code_to_file, zip_code_file
from utils.cache_manager import get_memory_list
from time import sleep
import sys

def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()

def show_architecture():
    arch = """
🏗️  Vibe Coding Architecture Overview:
─────────────────────────────────────
🔹 Model Loader      → Connects to local Ollama (LLaMA 3.3)
🔹 Vibe Coder        → Handles prompt + memory + clean code generation
🔹 Syntax Checker    → Verifies code structure by language
🔹 Tools Module      → Saves & compresses code to ZIP
🔹 Cache Manager     → Maintains recent code chat history (max 10)
🔹 Dataset Filter    → Prevents unsafe prompts
🔹 Typewriter        → Smooth, interactive CLI output
"""
    typewriter(arch, delay=0.005)

def main():
    print("💡 VibeCoder is ready! Type your coding prompt (type 'exit' to quit):")
    while True:
        user_input = input("Prompt > ")
        if user_input.lower() in ["exit", "quit"]:
            break
        filtered = filter_prompt(user_input)
        result = generate_code(filtered)
        typewriter("\n🧠 Generated Code:\n" + result)
        save_path = save_code_to_file(result)
        zip_path = zip_code_file(save_path)
        typewriter(f"📦 Your code has been zipped here: {zip_path}")
        show_architecture()
        print("\n📝 Previous Chat Summary:")
        for i, (u, a) in enumerate(get_memory_list(), 1):
            typewriter(f"{i}. You: {u}\n   AI: {a[:60]}...")

if __name__ == "__main__":
    main()
