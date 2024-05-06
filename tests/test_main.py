import pytest
from fastapi.testclient import TestClient
from ..tests import app

client = TestClient(app)

def test_predict():
    # Prueba básica para la ruta de predicción
    data = {"dato1": 1, "dato2": 2}  # Datos de ejemplo
    response = client.post("/predictionCepa", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
