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


response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
res = soup.find_all("li", class_="list-group-item")
print(res)
