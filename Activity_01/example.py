import requests


def get_coordinates(query):
    api_url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    headers = {"User-Agent": "my-app"}
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
    if not response_data:
        return None
    return float(response_data[0]["lat"]), float(response_data[0]["lon"])
