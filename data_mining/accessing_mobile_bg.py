from bs4 import BeautifulSoup
import urllib3
import time

http = urllib3.PoolManager()

URL = "https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=otr5yd&f1"


def generate_text_from_html(url_for_conversion):
    response = http.request('GET', url_for_conversion)
    soup = BeautifulSoup(response.data, "html.parser")
    return soup


# Get the last page - this will be used for the loop
def get_last_page(html_data):
    all_pages = html_data.find("span", {"class": "pageNumbersInfo"})
    # Extract only the last number
    last_page = all_pages.text.split(" ")[-1]
    return int(last_page)


last_page = get_last_page(generate_text_from_html(URL))


# Generate all pages for a provided link (there are multiple pages for a particular search result)
def list_of_all_pages(last_page_for_generation):
    list_of_urls = [URL + f"={page}" for page in range(1, last_page_for_generation + 1)]
    return list_of_urls


pages_with_car_offers = list_of_all_pages(last_page)


# Once we have all the pages one must gather all links for the actual cars.
def get_all_links_of_cars(list_of_pages_with_cars):
    all_cars = []
    for page in list_of_pages_with_cars:
        html_parsed = generate_text_from_html(page)
        all_cars_per_page_unfiltered = html_parsed.find_all("a", {"class": "mmm"})
        for car in all_cars_per_page_unfiltered:
            if len(car) > 0:
                all_cars.append('https://' + car['href'][2::])
        time.sleep(4)
    return all_cars


all_car_links = get_all_links_of_cars(pages_with_car_offers)

# Extract all necessery date for each car offer
def get_exact_data_for_each_car(url_link):
    # This gets the general stats of for each car
    link = generate_text_from_html(url_link)
    car_dict = {}
    general_data = link.find('ul', {'class': 'dilarData'}).findChildren("li", recursive=False)
    general_data_only_text = [info.text for count, info in enumerate(general_data) if count % 2 and count != 0]
    if len(general_data_only_text) == 8:
        car_dict[url_link] = {"General Data": {"Date of production": general_data_only_text[0], "Type of engine": general_data_only_text[1], "Horsepower": general_data_only_text[2], "Eurostandard": general_data_only_text[3], "Transmission": general_data_only_text[4], "Car type": general_data_only_text[5], "Kilometers traveled": general_data_only_text[6], "Colour": general_data_only_text[7]}}
    else:
        return
    # This gets the price of the car
    detailed_price = int(link.find('span', {'id': 'details_price'}).text.replace('лв.', '').replace(' ', ''))
    price_dict = {"Price": detailed_price}
    car_dict.update(price_dict)
    # Get all additional features
    additional_features = link.find_all('label', {'class': 'extra_cat'})
    specific_element = []
    for element in additional_features:
        for element1 in element.find_next_siblings('div'):
            specific_element.append(element1.text.replace('•', '').strip())
    additinal_elements_dict = {"Additional Data": specific_element}
    car_dict.update(additinal_elements_dict)

    return car_dict


def get_results_from_detailed_pages(list_to_append_to):
    for link in all_car_links:
        list_to_append_to.append(get_exact_data_for_each_car(link))
        time.sleep(3)
