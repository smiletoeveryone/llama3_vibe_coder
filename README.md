# 💡 VibeCoder: LLaMA 3.3 Local AI Coding Assistant

> A professional AI assistant built with LLaMA 3.3 (via Ollama) designed to help developers write, revise, and zip up code in real-time with architectural prompt reasoning, code memory, and typewriter-style output.

---

## 📌 Project Overview

VibeCoder is a local, intelligent developer assistant built using Apple-inspired modular architecture and local LLMs. It supports:

- 💬 Prompt-based code generation
- 💾 Local memory of prior interactions
- ⌨️ Typewriter effect output
- 📦 Auto ZIP download of generated code
- 🧠 Modular AI components mimicking Apple Foundation LLM architecture

---

## 🧠 Prompt Design Philosophy

System prompts follow this pattern:

> “You are a professional AI coding assistant. Help with: \<user request\>. Provide only clean and production-level code.”

Prompt chain includes prior chat history (up to 10), language context, and safety filters.

---

## 🏗️ Architecture Overview

```text
llama3_vibe_coder/
├── config/                # Model and language settings
│   ├── model_config.py
│   └── lang_support.py
├── core/                  # LLM interface and chat control
│   ├── model_loader.py    # Connects to Ollama + LLaMA 3.3
│   ├── vibe_coder.py      # Prompt + memory + code generation
│   └── tools.py           # Save + zip functions
├── data/
│   ├── dataset_filter.py  # Safety checks on input
│   └── coding_templates/  # Future extension
├── utils/
│   ├── cache_manager.py   # Chat history (max 10)
│   ├── quantization.py    # Placeholder for quantization simulation
│   └── syntax_checker.py  # Basic syntax structure check
├── app.py                 # Typewriter-style CLI interface
├── requirements.txt       # Python dependencies
└── README.md              # Project description

⚙️ Setup (Anaconda)

# Create environment
conda create -n vibe-coder python=3.10 -y
conda activate vibe-coder

# Install dependencies
pip install -r requirements.txt

# Pull and run LLaMA 3.3 using Ollama
ollama serve
ollama pull llama3

# Start the assistant
python app.py
