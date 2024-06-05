# # test_structural
# import pytest
# import example

# # Cheks that the structural functions of the solution
# # are calleable and that returns something


# def test_can_call_existing_endpoints_of_the_API():
#     try:
#         ret = example.get_coordinates("Lima")
#         assert ret is not None
#     except:
#         pass


# def test_cannot_call_non_existing_endpoints_of_the_API():
#     try:
#         ret = example.get_coordinates("Lima")
#         assert False, "No exception while calling a non existing function"
#     except:
#         pass


# def test_the_output_for_lima_is_correct():
#     expected = (-12.0621065, -77.0365256)
#     detected = example.get_coordinates("Lima")
#     assert (
#         abs(detected[0] - expected[0]) < 0.000001
#         and abs(detected[1] - expected[1]) < 0.000001
#     ), "The output for Lima is incorrect"

# def test_the_output_for_caracas_is_correct():
#     expected = (10.5060934, -66.9146008)
#     detected = example.get_coordinates("Caracas")
#     assert (
#         abs(detected[0] - expected[0]) < 0.000001
#         and abs(detected[1] - expected[1]) < 0.000001
#     ), "The output for Caracas is incorrect"

# def test_the_output_for_madrid_is_correct():
#     expected = (40.4167047, -3.7035825)
#     detected = example.get_coordinates("Madrid")
#     assert (
#         abs(detected[0] - expected[0]) < 0.000001
#         and abs(detected[1] - expected[1]) < 0.000001
#     ), "The output for Madrid is incorrect"

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

