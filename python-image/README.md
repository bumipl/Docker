# How to run python3 app in docker?

### 1. Create app.py

### 2. Create Dockerfile
```bash
cat <<EOF | tee Dockerfile
FROM python:latest
WORKDIR /app
COPY . /app
CMD ["python3","todo.py"]
EOF
```
### 3. Create docker container 
```bash
docker build -t todoapp .
```
### 4. Run docker container 
```bash
docker run -it todoapp
```
