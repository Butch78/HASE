from fastapi.testclient import TestClient
from src.main import app
from src.schemas import User, Item

client = TestClient(app)

def test_health():

    response = client.get("/health")

    assert(response.json() == {"status": "ok"})

def test_get_users():

    response = client.get("/users")

    assert(response.json()== list[User])

def test_get_items():

    response = client.get("/items")

    assert(response.json() == list[Item])

