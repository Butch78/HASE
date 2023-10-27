from fastapi.testclient import TestClient
from src.main import app
from src.schemas import UserCreate
from src.crud import create_user

client = TestClient(app)

def test_health():
    # Arrange
    expected_status_code = 200

    # Act
    response = client.get("/health")

    # Assert
    assert response.status_code == expected_status_code
    assert response.json() == {"status": "ok"}

def test_get_users():
    # Arrange
    expected_status_code = 200
    
    # Act
    response = client.get("/users")

    # Assert
    assert response.status_code == expected_status_code
    assert type(response.json()) == list

def test_get_items():
    # Arrange
    expected_status_code = 200
    
    # Act
    response = client.get("/items")

    # Assert
    assert response.status_code == expected_status_code
    assert type(response.json()) == list

