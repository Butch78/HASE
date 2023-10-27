from fastapi.testclient import TestClient
from src.main import app
from src.schemas import User, Item

client = TestClient(app)

def test_health():

    response = client.get("/health")

    assert(response.json() == {"status": "ok"})

def test_get_users():

    response = client.get("/users")

    assert(response.json()=={'email': 'john@test.com', 'id': 1, 'name': 'John Doe'}, {'email': 'jane@test.com', 'id': 2, 'name': 'Jane Doe'})

def test_get_items():

    response = client.get("/items")
    assert(response.json() == {'description': 'A Fruit!', 'id': 1, 'owner_id': 1, 'title': 'Apple'}, {'description': 'A Fruit!', 'id': 2, 'owner_id': 2, 'title': 'Pear'})

