import time
import requests
from bs4 import BeautifulSoup


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


URL = "https://www.emerita.legal/abogado/a/"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

req = requests.get(URL, headers)
soup = BeautifulSoup(req.content, 'html.parser')
res = soup.find_all("li", class_="list-group-item")
print(res)
