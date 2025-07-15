import requests
from config import API_KEY, API_BASE_URL

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def create_service(gig, day, test=0):
    payload = {"gig": gig, "day": day, "test": test}
    response = requests.post(API_BASE_URL + "create", json=payload, headers=HEADERS)
    return response.json()

def get_services():
    response = requests.get(API_BASE_URL + "clients", headers=HEADERS)
    return response.json()

def delete_service(username):
    response = requests.post(API_BASE_URL + "delsv", json={"username": username}, headers=HEADERS)
    return response.json()
