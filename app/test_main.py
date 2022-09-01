from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello_name():
    response = client.get("/fulano")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello fulano"}

def test_bye_name():
    response = client.get("/bye/fulano")
    assert response.status_code == 200
    assert response.json() == {"message": "Bye fulano"}

def test_sum():
    response = client.get("/sum/5/3")
    assert response.status_code == 200
    assert response.json() == {"message": f"The sum is {5 + 3}"}

def test_sub():
    response = client.get("/sub/5/3")
    assert response.status_code == 200
    assert response.json() == {"message": f"The sub is {5 - 3}"}
    
def test_mult():
    response = client.get("/mult/5/3")
    assert response.status_code == 200
    assert response.json() == {"message": f"The sum is {5 * 3}"}