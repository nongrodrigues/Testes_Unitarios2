import pytest
import threading
import time
import socket
import uvicorn
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def obter_porta_livre() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

@pytest.fixture(scope="session")
def server_url():
    porta = obter_porta_livre()
    config = uvicorn.Config(app=app, host="127.0.0.1", port=porta, log_level="critical")
    server = uvicorn.Server(config)
    
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    time.sleep(1.5) 
    
    yield f"http://127.0.0.1:{porta}"
    
    server.should_exit = True
    thread.join(timeout=2)