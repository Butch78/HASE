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

def test_create_user():
    # Arrange
    name = "John Doe"
    email = "johndoe@test.com"
    user = UserCreate(email="", name=name)
    expected_status_code = 200

    # Act
    response = client.post("/users", json=user.model_dump())

    # Assert
    assert response.status_code == expected_status_code
    assert response.json()["name"] == user.name
    assert response.json()["email"] == user.email

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

