from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
from selenium.webdriver.support.ui import Select

URL = "https://www.mobile.bg/pcgi/mobile.cgi"

# PATH = '/Applications/chromedriver' for mac
PATH = "C:\Windows\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(URL)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

all_car_brands = [brand.text.replace("\n", "") for brand in soup.find("select", {"name": "marka"}).findChildren("option", recursive=False)]


models = []
for brand in all_car_brands[5:20]:
    select = Select(driver.find_element_by_name("marka"))
    select.select_by_visible_text(brand)
    new_page_source = driver.page_source
    new_soup = BeautifulSoup(new_page_source, "html.parser")
    time.sleep(1)
    models.append({brand: [model.text for model in new_soup.find("select", {"name": "model"}).findChildren("option", recursive=False)]})
    

print(all_car_brands)
print(len(all_car_brands))
print(models)
print(len(models))