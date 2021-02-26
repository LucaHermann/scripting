import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint


class colors:  # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


# todo: finish the automation from a->z then 1->41
URL = 'https://www.emerita.legal/abogado/'

# setup selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-application-cache')
options.add_argument('--headless')
driver = webdriver.Chrome('../utils/chromedriver', options=options)

driver.get(URL)

html = driver.page_source
soup = BeautifulSoup(html, features="lxml")
print(soup)
results = soup.find_element_by_class_name("")
# href_elems = results.find_elements_by_xpath(
#     "/body/app-root/div/ng-sidebar-container/div/div/app-alphabetical-content/ul/li/a")

# for href_elem in href_elems:
#     elem = href_elem.find('a')
#     print(colors.RED + 'href' + elem.strip())

driver.close()
