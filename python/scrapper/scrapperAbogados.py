# import requested for script work
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


URL = 'https://www.emerita.legal/abogado/a'

# setup selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-application-cache')
options.add_argument('--headless')
driver = webdriver.Chrome('../utils/chromedriver', options=options)
driver.get(URL)

# Click the cookie button
# driver.find_element_by_class_name(
#     'hz-consents-banner').find_element_by_class_name('btn-primary').click()
# # Wait reload
# time.sleep(3)

# nbrTelephones = len(driver.find_elements_by_class_name(
#     'hz-pro-search-result__right-info__contact-info'))

nbrClient = len(driver.find_element_by_class_name(
    "list-group-item col-6 ng-star-inserted"))

# For every div where there is a span containing a telephone number
# for telephone in range(1, nbrTelephones):
#     # Click each span containing a telephone number
#     driver.find_element_by_class_name(
#         'hz-pro-search-result__contact-info__cover').click()
#     # Wait reload
#     time.sleep(1)

for client in range(1, nbrClient):
    driver.find_elements_by_xpath("//a[@href]")

html = driver.page_source
soup = BeautifulSoup(html, features="lxml")
results = soup.find(id='fix-header card-no-border logo-center ng-tns-0-1')
companies_elems = results.find_all("a")
# Loop over each elem(1 elem is 1 customer)
# for company_elem in companies_elems:
#     company_name_elem = company_elem.find(
#         'span', class_='header-5 text-unbold mlm')
#     telephone_number_elem = company_elem.find(
#         'span', class_='hz-pro-search-result__contact-info')
#     location_elem = company_elem.find(
#         'span', class_='hz-pro-search-result__location-info__text')
#     if None in (company_name_elem, telephone_number_elem, location_elem):
#         continue
#     print(colors.RED + 'company_name:' +
#           colors.ENDC, company_name_elem.text.strip())
#     print(colors.RED + 'telephone_number' +
#           colors.ENDC, telephone_number_elem.text.strip())
#     print(colors.RED + 'location:' + colors.ENDC, location_elem.text.strip())
print(companies_elems)
