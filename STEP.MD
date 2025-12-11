ggwp@ggwp-B660M-Pro-RS:~/code/coba$ curl -fsSL https://ollama.com/install.sh | sh
>>> Installing ollama to /usr/local
[sudo] password for ggwp: 
Sorry, try again.
[sudo] password for ggwp: 
>>> Downloading Linux amd64 bundle
######################################################################## 100.0%
>>> Creating ollama user...
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
ggwp@ggwp-B660M-Pro-RS:~/code/coba$ ollama --version
ollama version is 0.13.2
ggwp@ggwp-B660M-Pro-RS:~/code/coba$ ollama pull llama3
ggwp@ggwp-B660M-Pro-RS:~/code/coba$ ollama run llama3

