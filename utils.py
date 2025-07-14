import requests
from config import API_KEY, API_BASE

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def create_service(gig, day, test=0):
    data = {"gig": gig, "day": day, "test": test}
    res = requests.post(API_BASE + "create", json=data, headers=HEADERS)
    return res.json()

def get_services():
    res = requests.get(API_BASE + "clients", headers=HEADERS)
    return res.json()

def delete_service(username):
    res = requests.post(API_BASE + "delsv", json={"username": username}, headers=HEADERS)
    return res.json()
