# tests/test_customers.py

from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_customer():
    payload = {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "address": "101 Maple St",
        "phone_number": "555-1234"
    }

    # Test POST /customers/
    response = client.post("/customers/", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Verify returned data
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data

    # Test GET /customers/{id}
    customer_id = data["id"]
    get_response = client.get(f"/customers/{customer_id}")
    assert get_response.status_code == 200
    retrieved_data = get_response.json()
    assert retrieved_data["name"] == payload["name"]
