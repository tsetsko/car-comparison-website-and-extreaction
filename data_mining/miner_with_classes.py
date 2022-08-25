import time
from datetime import datetime
from sys import platform
import pandas as pd
from bs4 import BeautifulSoup
import requests


class CarModels:
    def __init__(self):
        self.car_models_list = list(pd.read_excel('car_brands_and_models_links_VW.xlsx').itertuples(index=False, name=None))

URL = "https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=padj4g&f1"
TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')


def get_page_source(url, header):
    responce = requests.get(url, header)
    soup = BeautifulSoup(responce.content, 'html.parser')
    return soup


class PageHandler:
    def __init__(self, url: str) -> None:
        self.month_to_number = {"януари": 1, "февруари": 2, "март": 3, "април": 4, "май": 5, "юни": 6, "юли": 7, "август": 8, "септември": 9, "октовмри": 10, "ноември": 11, "декември": 12}
        self.platform = self.get_platform()
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        self.url = url
        self.list_of_urls = self.get_all_pages_pagination()
        self.all_car_links = self.extract_car_links_per_page()

    def get_platform(self):
        path = ""
        if platform == "darwin":
            path = '/Applications/chromedriver'
        elif platform == "win32":
            path = "C:\Windows\chromedriver.exe"
        return path

    def get_all_pages_pagination(self):
        all_pages = get_page_source(self.url, self.header).find("span", {"class": "pageNumbersInfo"})
        last_page = all_pages.text.split(' ')[-1]
        list_of_urls = [self.url + f"={page}" for page in range(1, int(last_page) + 1)]
        return list_of_urls

    def extract_car_links_per_page(self):
        intermediate_list = []
        for list_page in self.list_of_urls:
            cars_per_page = get_page_source(list_page, self.header).find_all("a", {"class": "mmm"})
            for car_link in cars_per_page:
                if len(car_link) > 0:
                    intermediate_list.append('https://' + car_link['href'][2::])
        return intermediate_list


# link = PageHandler(URL).extract_car_links_per_page()
# print(link)


class CarPage:
    def __init__(self, link_for_car, brand, model):
        self.EUR_TO_LEV = 1.95583
        self.TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')
        self.month_to_number = {"януари": 1, "февруари": 2, "март": 3, "април": 4, "май": 5, "юни": 6, "юли": 7,
                                "август": 8, "септември": 9, "октовмри": 10, "ноември": 11, "декември": 12}
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        self.brand = brand
        self.model = model
        self.link_for_car = link_for_car
        self.car_details = self.get_exact_data_for_each_car()

    def get_exact_data_for_each_car(self):
        car_dict = {}
        try:
            car_dict['Brand'] = self.brand
            car_dict['Model'] = self.model
            general_data = get_page_source(self.link_for_car, self.header).find('ul', {'class': 'dilarData'}).findChildren("li", recursive=False)
            general_data_only_text = [info.text for info in general_data]
            car_dict["Date_of_extraction"] = self.TODAYS_DATE
            if "Дата на производство" in general_data_only_text:
                month_of_production_index = general_data_only_text.index("Дата на производство") + 1
                car_dict["Month_of_production"] = int(self.month_to_number.get(general_data_only_text[month_of_production_index].split(" ")[0]))
                car_dict["Year_of_production"] = int(general_data_only_text[month_of_production_index].split(" ")[1].replace("г.", ""))
            else:
                car_dict["Month_of_production"] = -1
                car_dict["Year_of_production"] = -1
            if "Тип двигател" in general_data_only_text:
                type_of_engine_index = general_data_only_text.index("Тип двигател") + 1
                car_dict["Type_of_engine"] = general_data_only_text[type_of_engine_index]
            else:
                car_dict["Type_of_engine"] = '-1'
            if "Мощност" in general_data_only_text:
                horsepower = general_data_only_text.index("Мощност") + 1
                car_dict["Horsepower"] = float(general_data_only_text[horsepower].split(" ")[0])
            else:
                car_dict["Horsepower"] = -1
            if "Евростандарт" in general_data_only_text:
                eurostandard = general_data_only_text.index("Евростандарт") + 1
                car_dict["Eurostandard"] = general_data_only_text[eurostandard]
            else:
                car_dict["Eurostandard"] = '-1'
            if "Скоростна кутия" in general_data_only_text:
                transmission = general_data_only_text.index("Скоростна кутия") + 1
                car_dict["Transmission"] = general_data_only_text[transmission]
            else:
                car_dict["Transmission"] = '-1'
            if "Категория" in general_data_only_text:
                car_type = general_data_only_text.index("Категория") + 1
                car_dict["Car_type"] = general_data_only_text[car_type]
            else:
                car_dict["Car_type"] = '-1'
            if "Пробег" in general_data_only_text:
                kilometers_traveled = general_data_only_text.index("Пробег") + 1
                car_dict["Kilometers_traveled"] = float(general_data_only_text[kilometers_traveled].split(" ")[0])
            else:
                car_dict["Kilometers_traveled"] = -1
            if "Цвят" in general_data_only_text:
                colour = general_data_only_text.index("Цвят") + 1
                car_dict["Colour"] = general_data_only_text[colour]
            else:
                car_dict["Colour"] = '-1'
            # This gets the price of the car
            detailed_price_general = get_page_source(self.link_for_car, self.header).find('span', {'id': 'details_price'}).text
            if "лв." in detailed_price_general:
                detailed_price = int(detailed_price_general.replace('лв.', '').replace(" ", ""))
            else:
                detailed_price = round(int(detailed_price_general.replace('EUR', '').replace(" ", "")) * self.EUR_TO_LEV, 0)
            car_dict["Price"] = detailed_price
            # Get all additional features
            additional_features = get_page_source(self.link_for_car, self.header).find_all('label', {'class': 'extra_cat'})
            specific_element = []
            for element in additional_features:
                for element1 in element.find_next_siblings('div'):
                    specific_element.append(element1.text.replace('•', '').strip())
            car_dict["Additional_Data"] = ', '.join(specific_element)
            print(car_dict["Additional_Data"])
            car_dict["link_to_offer"] = self.link_for_car
        except:
            pass

        return car_dict


car_models = CarModels().car_models_list

main_list = []
for car_model in car_models:
    brand = car_model[1]
    model = car_model[2]
    model_url = car_model[3][:-2]
    print(f"The model link is: {model_url}")
    links = PageHandler(model_url).extract_car_links_per_page()
    print('passed')
    for link in links:
        car = CarPage(link, brand, model)
        time.sleep(1)
        main_list.append(car.car_details)
        print("extracted detailed data")


df = pd.DataFrame.from_dict(main_list)
df2 = df.dropna().reset_index(drop=True)

print(df2)

df2.to_excel(f"data_{TODAYS_DATE}_VW.xlsx")

