import requests

headers = {
    "X-Auth-Token": "17148893d37d4defabba62e19628373f"
}

r = requests.get(
    "https://api.football-data.org/v4/matches",
    headers=headers
)

print(r.status_code)
print(r.text[:1000])