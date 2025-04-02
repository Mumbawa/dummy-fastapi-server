from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/hello")
def read_hello():
    return {
        "message": "Hello, world!",
        "hostname": socket.gethostname(),
    }


@app.get("/health-check")
def read_health_check():
    return {
        "status": "healthy",
    }
