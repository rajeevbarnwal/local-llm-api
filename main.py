from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import os

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(prompt: Prompt):
    try:
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3:latest")

        response = requests.post(
            f"{ollama_host}/api/generate",
            json={"model": ollama_model, "prompt": prompt.prompt},
            stream=True,
            timeout=120
        )
        response.raise_for_status()

        output = ""
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8").strip()
                if data.startswith("data: "):
                    data = data[len("data: "):]
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                    output += chunk.get("response") or chunk.get("text") or ""
                except json.JSONDecodeError:
                    continue

        return {"response": output.strip() or "(Empty response from model)"}
    except requests.RequestException as e:
        return {"error": f"Ollama request failed: {str(e)}"}
