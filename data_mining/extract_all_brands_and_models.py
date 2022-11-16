from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
from sys import platform

URL = "https://www.mobile.bg/pcgi/mobile.cgi"

path = ""
if platform == "darwin":
    path = '/Applications/chromedriver'
elif platform == "win32":
    path = "C:\Windows\chromedriver.exe"
# PATH = "/Applications/geckodriver"
BRANDS_TO_LOOK_FOR = ["BMW"]
BRANDS_TO_LOOK_FOR1 = ["Audi", "BMW", "Mercedes-Benz", "Skoda", "VW"]
AUDI_MODELS = ['A1', 'A2', 'A3', 'A4', 'A4 Allroad', 'A5', 'A6', 'A6 Allroad', 'A7', 'A8', 'E-Tron', 'Q2', 'Q3', 'Q4', 'Q5', 'Q7', 'Q8', 'Quattro', 'R8', 'RSQ8', 'Rs3', 'Rs4', 'Rs5', 'Rs6', 'Rs7', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'SQ5', 'SQ7', 'SQ8', 'Tt']
BMW_MODELS = ['1', '2', '3', '4', '5', '6', '7', 'M', 'M Coupе', 'M135', 'M140', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'X1', 'X2', 'X3', 'X4', 'X5', 'X5M', 'X6', 'X7', 'Z1', 'Z3', 'Z4', 'Z8', 'i3', 'i4', 'i8', 'iX', 'iX3']
MECEDES_MODELS = ['A', 'AMG GT', 'AMG GT C', 'AMG GT R', 'AMG GT S', 'Adenauer', 'B', 'C', 'CL', 'CLA', 'CLC', 'CLK', 'CLS', 'E', 'EQA', 'EQB', 'EQC', 'EQE', 'EQS', 'EQV', 'G', 'GL', 'GLA', 'GLB', 'GLC', 'GLE', 'GLK', 'GLS', 'GT', 'GTS', 'ML', 'Maybach', 'R', 'S', 'SL', 'SLC', 'SLK', 'SLR', 'SLS', 'SLS AMG', 'Vaneo', 'Viano', 'X-Klasse']
SKODA_MODELS = ['Citigo', 'Enyaq', 'Fabia', 'Forman', 'Kamiq', 'Karoq', 'Kodiaq', 'Octavia', 'Praktik', 'Rapid', 'Roomster', 'Scala', 'Superb', 'Yeti']
VW_MODELS = ['Alltrack', 'Amarok', 'Arteon', 'Atlas', 'Bora', 'CC', 'Caddy', 'Corrado', 'Derby', 'Eos', 'Golf', 'Golf Plus', 'Golf Variant', 'ID.3', 'ID.4', 'Jetta', 'Lupo', 'Multivan', 'New beetle', 'Passat', 'Phaeton', 'Polo', 'Rabbit', 'Santana', 'Scirocco', 'Sharan', 'Sportsvan', 'T-Cross', 'T-Roc', 'Taro', 'Tiguan', 'Touareg', 'Touran', 'Up', 'Vento']
# PATH = "C:\Windows\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(URL)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

all_car_brands = [brand.text.replace("\n", "") for brand in soup.find("select", {"name": "marka"}).findChildren("option", recursive=False) if brand.text != "всички\n"]
print(all_car_brands)

models = []
for brand in all_car_brands:
    if brand in BRANDS_TO_LOOK_FOR:
        select = Select(driver.find_element(By.NAME, "marka"))
        select.select_by_visible_text(brand)
        new_page_source = driver.page_source
        new_soup = BeautifulSoup(new_page_source, "html.parser")
        model_to_loop = [model.text for model in new_soup.find("select", {"name": "model"}).findChildren("option", recursive=False) if model.text in BMW_MODELS]
        # model_to_loop = [AUDI_MODELS]
        print(model_to_loop)
        for model in model_to_loop:
            # I do this to get rid of the initial popup
            try:
                driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
                driver.implicitly_wait(1)
            except:
                pass
            # First always select the "всички" category so that the models for the different brands can be refreshed.
            driver.find_element(By.NAME, "marka").click()
            driver.implicitly_wait(2)
            general_select = Select(driver.find_element(By.NAME, "marka"))
            driver.implicitly_wait(2)
            general_select.select_by_visible_text("всички")
            # This is the selector for the brand
            driver.find_element(By.NAME, "marka").click()
            time.sleep(1)
            brand_select = Select(driver.find_element(By.NAME, "marka"))
            brand_select.select_by_visible_text(brand)
            driver.implicitly_wait(2)
            # This is the selector for the model
            driver.find_element(By.NAME, "model").click()
            driver.implicitly_wait(2)
            model_select = Select(driver.find_element(By.NAME, "model"))
            model_select.select_by_value(model)
            driver.implicitly_wait(2)
            driver.find_element(By.ID, "button2").click()
            driver.implicitly_wait(2)
            current_url = driver.current_url
            where_to_look_for = brand + "-" + model
            models.append({"Maker": brand, "Model": model, "URL": current_url})
            time.sleep(5)
            driver.execute_script("window.history.go(-1)")
            time.sleep(2)
            df = pd.DataFrame.from_dict(models)
            print(df)
            df.to_excel(f"car_brands_and_models_links_BMW.xlsx")
    time.sleep(2)

print(models)