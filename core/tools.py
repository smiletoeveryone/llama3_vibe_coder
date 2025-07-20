# Tools for file saving, zip packaging
import os
import zipfile

def save_code_to_file(code: str, filename: str = "output.py"):
    with open(filename, "w") as f:
        f.write(code)
    return filename

def zip_code_file(filepath: str) -> str:
    zip_path = filepath.replace(".py", ".zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(filepath)
    return zip_path
