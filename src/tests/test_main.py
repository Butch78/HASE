from fastapi.testclient import TestClient
from src.main import app
from src.schemas import UserCreate, ItemCreate
from src.crud import create_user

client = TestClient(app)

def test_health():
    # Arrange

    # Act
    response = client.get("/health")

    # Assert
    assert response.json() == {"status": "ok"}

def test_get_users():
    # Arrange
    
    # Act
    response = client.get("/users")

    # Assert
    assert(response.json()== list[UserCreate])

def test_get_items():
    # Arrange
    
    # Act
    response = client.get("/items")

    # Assert
    assert(response.json() == list[ItemCreate])

