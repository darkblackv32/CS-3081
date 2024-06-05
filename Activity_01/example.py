# import requests


# def get_coordinates(query):
#     api_url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
#     headers = {"User-Agent": "my-app"}
#     response = requests.get(api_url, headers=headers)
#     response_data = response.json()
#     # if not response_data:
#         # return None
#     return float(response_data[0]["lat"]), float(response_data[0]["lon"])

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class QueryModel(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Coordinates API"}

@app.post("/get-coordinates/")
def get_coordinates(query: QueryModel):
    api_url = f"https://nominatim.openstreetmap.org/search?q={query.query}&format=json"
    headers = {"User-Agent": "my-app"}
    response = requests.get(api_url, headers=headers)
    response_data = response.json()

    if not response_data:
        raise HTTPException(status_code=404, detail="Location not found")

    lat = float(response_data[0]["lat"])
    lon = float(response_data[0]["lon"])
    return {"latitude": lat, "longitude": lon}
