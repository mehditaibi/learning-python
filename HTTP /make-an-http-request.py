import requests

url = "https://google.com"
response = requests.get(url)

response.ok # True or False
response.headers # to see headers
response.text 


