import requests
import json

base_url = "http://127.0.0.1:8000"
username = "admin2@test.com"
password = "123456"

# 1. Login
print("Logging in...")
resp = requests.post(f"{base_url}/token/", json={'username': username, 'password': password})
if resp.status_code != 200:
    print("Login failed:", resp.text)
    exit(1)

data = resp.json()
token = data['token']
print("Login successful. Token obtained.")

headers = {'Authorization': f'Bearer {token}'}

# 2. Verify Lists
endpoints = ['lista-admins', 'lista-alumnos', 'lista-maestros']

for ep in endpoints:
    print(f"\nVerifying {ep}...")
    r = requests.get(f"{base_url}/{ep}/", headers=headers)
    if r.status_code == 200:
        print(f"SUCCESS: {ep} returned {len(r.json())} items.")
        # print(json.dumps(r.json(), indent=2))
    else:
        print(f"FAILED: {ep} returned {r.status_code}")
        print(r.text)
