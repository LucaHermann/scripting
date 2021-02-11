import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.houzz.es/professionals/instalacion-y-reformas-de-cocinas-y-banos/c/Madrid/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, features="lxml")
rawData = soup.find("script", id="hz-ctx")
cleanedData = str(rawData).replace('<script id="hz-ctx" type="application/json">',
                                   "").replace('</script>', "")
arr = json.loads(cleanedData)
pprint(arr)
