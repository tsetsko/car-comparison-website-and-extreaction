from selenium import webdriver

PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

URL = "https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=ow9ic6&f1=1"

driver.get(URL)
print(driver.page_source)