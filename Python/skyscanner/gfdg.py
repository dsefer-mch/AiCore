import requests

response = requests.get('https://www.skyscanner.net/')
print(response.json)
response.json