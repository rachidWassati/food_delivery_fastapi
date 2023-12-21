from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_restaurant():
    sample_payload = {
            "name": "Le Petit Bistro",
            "ownerName": "Isabelle Dupont",
            "foodTypes": ["French", "Seafood"],
            "postalcode": "75001",
            "address": "10 Rue de la Roquette",
            "phone": "01 45 67 89 10",
            "email": "lepetitbistro@gmail.com",
            "password": "qwerty"
        }
    response = client.post("/api/v1/admin/restaurants", json=sample_payload)
    assert response.status_code == 201
    assert response.json() == {
    "status": "success",
    "restaurant": {
        "id": "65848754fb9ec183316de39c",
        "ownerName": "Isabelle Dupont",
        "foodTypes": [
            "French",
            "Seafood"
        ],
        "postalcode": "75001",
        "address": "10 Rue de la Roquette",
        "phone": "01 45 67 89 10",
        "email": "lepetitbistro@gmail.com",
        "serviceAvailable": "false",
        "coverImages": [],
        "rating": 0.0
    }
}
