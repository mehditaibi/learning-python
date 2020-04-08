import requests

url = "https://icanhzdadjoke.com/"
response = requests.get(
    url,
    headers={
        "Accept": "application/json"
    }
)

print(response.json())