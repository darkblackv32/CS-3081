import pytest
from fastapi.testclient import TestClient
from example import app  

client = TestClient(app)

def test_can_call_existing_endpoints_of_the_API():
    response = client.post("/get-coordinates/", json={"query": "Lima"})
    assert response.status_code == 200
    assert response.json() is not None

def test_cannot_call_non_existing_endpoints_of_the_API():
    response = client.post("/non-existing-endpoint", json={"query": "Lima"})
    assert response.status_code == 404

def test_the_output_for_lima_is_correct():
    expected = {"latitude": -12.0621065, "longitude": -77.0365256}
    response = client.post("/get-coordinates/", json={"query": "Lima"})
    assert response.status_code == 200
    detected = response.json()
    assert (
        abs(detected["latitude"] - expected["latitude"]) < 0.000001
        and abs(detected["longitude"] - expected["longitude"]) < 0.000001
    ), "The output for Lima is incorrect"

def test_the_output_for_caracas_is_correct():
    expected = {"latitude": 10.5060934, "longitude": -66.9146008}
    response = client.post("/get-coordinates/", json={"query": "Caracas"})
    assert response.status_code == 200
    detected = response.json()
    assert (
        abs(detected["latitude"] - expected["latitude"]) < 0.000001
        and abs(detected["longitude"] - expected["longitude"]) < 0.000001
    ), "The output for Caracas is incorrect"

def test_the_output_for_madrid_is_correct():
    expected = {"latitude": 40.4167047, "longitude": -3.7035825}
    response = client.post("/get-coordinates/", json={"query": "Madrid"})
    assert response.status_code == 200
    detected = response.json()
    assert (
        abs(detected["latitude"] - expected["latitude"]) < 0.000001
        and abs(detected["longitude"] - expected["longitude"]) < 0.000001
    ), "The output for Madrid is incorrect"

