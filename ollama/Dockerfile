FROM ubuntu:22.04

ENV OLLAMA_HOST=0.0.0.0:11434

# Install dependencies
RUN apt update && \
    apt install -y curl wget iputils-ping dnsutils && \
    rm -rf /var/lib/apt/lists/*

# Install Ollama (manual download binary)
RUN curl -L https://github.com/ollama/ollama/releases/download/v0.13.3/ollama-linux-amd64.tgz \
    -o /tmp/ollama.tgz && \
    tar -xzf /tmp/ollama.tgz -C /tmp && \
    mv /tmp/bin/ollama /usr/local/bin/ollama && \
    chmod +x /usr/local/bin/ollama && \
    rm -rf /tmp/*

# Expose port
EXPOSE 11434

# Start Ollama server
CMD ["ollama", "serve"]
