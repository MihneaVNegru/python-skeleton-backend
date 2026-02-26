import random
import string

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def test_signup_and_login():
    username = get_random_string(8)
    email = f"{username}@example.com"
    password = "testpassword123"

    # Test Signup
    signup_response = client.post(
        "/api/auth/signup",
        json={"username": username, "email": email, "password": password}
    )
    assert signup_response.status_code == 200
    assert signup_response.json()["username"] == username

    # Test Login
    login_response = client.post(
        "/api/auth/login",
        data={"username": username, "password": password}
    )
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    token = login_response.json()["access_token"]

    # Test protected route (Items)
    items_response = client.get(
        "/api/items/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert items_response.status_code == 200
