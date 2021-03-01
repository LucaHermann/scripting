# import requested for script work
import json
import requests
import time

response = requests.get(
    'https://www.emerita.legal/abogado/a')
rawHTML = response.content
print(rawHTML)
