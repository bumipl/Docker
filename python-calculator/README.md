# How to run python3 app in docker?

### 1. Create app.py

### 2. Create Dockerfile
```bash
cat <<EOF | tee Dockerfile
FROM python:latest
WORKDIR /calculator
COPY . /calculator/
CMD ["python3","calculator.py"]
EOF
```
### 3. Create docker container 
```bash
docker build -t calculator .
```
### 4. Run docker container 
```bash
xhost +local:docker  # Allow Docker containers to access the X server
docker run -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    calculator
```
