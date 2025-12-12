#!/bin/bash
set -e

# Start Ollama server in background
ollama serve &
sleep 5

# Pull the model
ollama pull llama3:latest

# Wait (keep server foreground)
wait -n
