uvicorn main:app --reload --host 0.0.0.0 --port 8000

docker run --rm --network=host alpine ping -c 4 google.com

docker build -t fastapi-app ./backend --network=host


