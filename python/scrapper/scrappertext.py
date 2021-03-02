import requests

response = requests.get(
    'https://www.emerita.legal/abogado/a')

print(response.content)
