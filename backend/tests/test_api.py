import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Bienvenue sur l'API M-Motors"


def test_create_vehicle():
    response = client.post("/vehicles", json={
        "marque": "Renault",
        "modele": "Clio",
        "prix": 12000,
        "type_offre": "vente"
    })

    assert response.status_code == 200
    assert response.json()["marque"] == "Renault"


def test_get_vehicles():
    response = client.get("/vehicles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_register_user():
    response = client.post("/register", json={
        "nom": "Client Test",
        "email": "client@test.fr",
        "mot_de_passe": "test123",
        "role": "client"
    })

    assert response.status_code in [200, 400]


def test_create_dossier():
    response = client.post("/dossiers", json={
        "user_email": "client@test.fr",
        "vehicle_id": 1,
        "type_demande": "location"
    })

    assert response.status_code == 200
    assert response.json()["statut"] == "en_attente"