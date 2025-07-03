#!/bin/bash
# Activate venv and run FastAPI server
source venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8080 --reload
