import requests

url = "https://icanhzdadjoke.com/search"
response = requests.get(
    url,
    headers={
        "Accept": "application/json"
    },
    params={
        "page": 1,
        "limit": 20,
        "term": "cat"
    }
)

data = response.json()
print(data["results"])
