
# How to use

## Instalation

1. docker compose build --no-cache

2. docker compose up

3. hit with bruno 
    curl --request GET --url http://0.0.0.0:8000/

4. hit check model available
    curl --request GET --url http://0.0.0.0:8000/check
    wait until "ollama_response" "models" available

## Registration and Ask AI

1. register the user
curl --request POST \
  --url http://0.0.0.0:8000/register \
  --header 'content-type: application/json' \
  --data '{
  "username": "r",
  "password": "r"
}'

2. get a token auth
curl --request POST \
  --url http://0.0.0.0:8000/token \
  --header 'content-type: multipart/form-data' \
  --form username=r \
  --form password=r

3. use token authorization and ask to /chat
curl --request POST \
  --url http://0.0.0.0:8000/chat \
  --header 'authorization: Bearer eyJh...' \
  --header 'content-type: application/json' \
  --data '{
  "message": "Rumah makan surabaya"
}'


# Self Docs

## OLLAMA LOCAL
sudo systemctl start ollama
sudo systemctl status ollama
sudo systemctl stop ollama

ollama list
llama3:latest    365c0bd3c000    4.7 GB

## OLLAMA DOCKER
docker build -t ollamaai ./ollama --no-cache
docker run -p 11434:11434 ollamaai
docker run --name ollamaai --network=host -v ollama_data:/root/.ollama ollama-ai

docker build -t ollama-full ./ollama/ --network=host
docker run --name ollama-full -p 11434:11434 -v ollama_data:/root/.ollama ollama-full
docker run --name ollama-full -p 11434:11434 -v ollama_data:/root/.ollama -e OLLAMA_HOST=0.0.0.0:11434 ollama-full

### use
docker build -t ollama-full ./ollama --network=host
docker rm ollama-full
docker run --name ollama-full --network=host -p 11434:11434 -v ollama_data:/root/.ollama -e OLLAMA_HOST=0.0.0.0:11434 ollama-full

## BACKEND
uvicorn main:app --reload --host 0.0.0.0 --port 8000

docker run --rm --network=host alpine ping -c 4 google.com

docker build -t fastapi-app ./backend --network=host --no-cache
docker run -p 8000:8000 fastapi-app

### use
docker build -t fastapi-app ./backend --network=host --no-cache
docker rm fastapi-app
docker run --name fastapi-app --network=host   -p 8000:8000   fastapi-app

## DOCKER
docker compose down -v
docker compose up --build --no-cache

docker network create mynet

### use
docker compose build --no-cache
docker compose up -d
