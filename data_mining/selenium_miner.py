import time
from datetime import datetime
import random
from sys import platform

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=oxonz5&f1"
EUR_TO_LEV = 1.95583
TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')
month_to_number = {"януари": 1, "февруари": 2, "март": 3, "април": 4, "май": 5, "юни": 6, "юли": 7, "август": 8, "септември": 9, "октовмри": 10, "ноември": 11, "декември": 12}


def get_page_source_with_selenium(url_link):
    path = ""
    if platform == "darwin":
        path = '/Applications/chromedriver'
    elif platform == "win32":
        path = "C:\Windows\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(url_link)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    return soup


def get_last_page(html_data):
    all_pages = html_data.find("span", {"class": "pageNumbersInfo"})
    # Extract only the last number
    last_page = all_pages.text.split(" ")[-1]
    return int(last_page)


last_page = get_last_page(get_page_source_with_selenium(URL))


# Generate all pages for a provided link (there are multiple pages for a particular search result)
def list_of_all_pages(last_page_for_generation):
    list_of_urls = [URL + f"={page}" for page in range(1, last_page + 1)]
    return list_of_urls


pages_with_car_offers = list_of_all_pages(last_page)


# Once we have all the pages one must gather all links for the actual cars.
def get_all_links_of_cars(html_parsed, list_to_append):
    all_cars_per_page_unfiltered = html_parsed.find_all("a", {"class": "mmm"})
    for car in all_cars_per_page_unfiltered:
        if len(car) > 0:
            list_to_append.append('https://' + car['href'][2::])


def get_exact_data_for_each_car(html_link):
    car_dict = {}
    try:
        general_data = html_link.find('ul', {'class': 'dilarData'}).findChildren("li", recursive=False)
        general_data_only_text = [info.text for info in general_data]
        car_dict["Date_of_extraction"] = TODAYS_DATE
        if "Дата на производство" in general_data_only_text:
            month_of_production_index = general_data_only_text.index("Дата на производство") + 1
            car_dict["Month_of_production"] = int(month_to_number.get(general_data_only_text[month_of_production_index].split(" ")[0]))
            car_dict["Year_of_production"] = int(general_data_only_text[month_of_production_index].split(" ")[1].replace("г.", ""))
        if "Тип двигател" in general_data_only_text:
            type_of_engine_index = general_data_only_text.index("Тип двигател") + 1
            car_dict["Type_of_engine"] = general_data_only_text[type_of_engine_index]
        if "Мощност" in general_data_only_text:
            horsepower = general_data_only_text.index("Мощност") + 1
            car_dict["Horsepower"] = float(general_data_only_text[horsepower].split(" ")[0])
        if "Евростандарт" in general_data_only_text:
            eurostandard = general_data_only_text.index("Евростандарт") + 1
            car_dict["Eurostandard"] = general_data_only_text[eurostandard]
        if "Скоростна кутия" in general_data_only_text:
            transmission = general_data_only_text.index("Скоростна кутия") + 1
            car_dict["Transmission"] = general_data_only_text[transmission]
        if "Категория" in general_data_only_text:
            car_type = general_data_only_text.index("Категория") + 1
            car_dict["Car_type"] = general_data_only_text[car_type]
        if "Пробег" in general_data_only_text:
            kilometers_traveled = general_data_only_text.index("Пробег") + 1
            car_dict["Kilometers_traveled"] = float(general_data_only_text[kilometers_traveled].split(" ")[0])
        if "Цвят" in general_data_only_text:
            colour = general_data_only_text.index("Цвят") + 1
            car_dict["Colour"] = general_data_only_text[colour]
        # This gets the price of the car
        detailed_price_general = html_link.find('span', {'id': 'details_price'}).text
        # detailed_price = 0
        if "лв." in detailed_price_general:
            detailed_price = int(detailed_price_general.replace('лв.', '').replace(" ", ""))
        else:
            detailed_price = round(int(detailed_price_general.replace('EUR', '').replace(" ", "")) * EUR_TO_LEV, 0)
        car_dict["Price"] = detailed_price
        # Get all additional features
        additional_features = html_link.find_all('label', {'class': 'extra_cat'})
        specific_element = []
        for element in additional_features:
            for element1 in element.find_next_siblings('div'):
                specific_element.append(element1.text.replace('•', '').strip())
        car_dict["Additional_Data"] = specific_element
    except:
        pass

    return car_dict


all_cars = []
for page in pages_with_car_offers:
    page_source = get_page_source_with_selenium(page)
    get_all_links_of_cars(page_source, all_cars)
    time.sleep(3)

all_data_list = []
counter = 0
for detailed_page in all_cars:
    random_delay = round(random.uniform(3, 6), 2)
    page_source_detail = get_page_source_with_selenium(detailed_page)
    detailed_dict = get_exact_data_for_each_car(page_source_detail)
    all_data_list.append(detailed_dict)
    counter += 1
    print(counter)
    time.sleep(random_delay)


df = pd.DataFrame.from_dict(all_data_list)
df2 = df.dropna().reset_index(drop=True)

print(df2)

df2.to_excel(f"data_{TODAYS_DATE}.xlsx")
