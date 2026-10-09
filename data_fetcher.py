import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """
    Fetches animal data from the API.
    Returns a list of animals.
    """
    api_url = "https://api.api-ninjas.com/v1/animals"

    response = requests.get(
        api_url,
        params={"name": animal_name},
        headers={"X-Api-Key": "API_KEY"}
    )

    if response.status_code == requests.codes.ok:
        return response.json()

    return None