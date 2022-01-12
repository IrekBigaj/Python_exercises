# #100days of code - day 48-49 - Selenium Driver
# Important data are stored in config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

CHROME_DRIVER_PATH = "C:\_Web\ChromeDriver\chromedriver.exe"

serv = Service(CHROME_DRIVER_PATH)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=opt)

# driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH) # wywołanie po staremu - zgłasza obecnie błąd
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/CanaKit-Raspberry-Pi-Extreme-Kit/dp/B08B6G2RFG/")
driver.get("https://www.python.org/")


# price = driver.find_element_by_class_name("a-offscreen")
# price = driver.find_element(By.CLASS_NAME = "")
# name = driver.find_element(By.ID, "productTitle")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# search = driver.find_element(By.NAME, "field-keywords")  # input field
# another = driver.find_element(By.XPATH, '//*[@id="bylineInfo"]')
# another2 = driver.find_element(By.XPATH, '//*[@id="price_inside_buybox"]')
#
#
# print(name.text)
# print(price.text)
# print(search.tag_name)
# print(another.text)

events_dic = {}

# events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

for n in range(0, len(events_times)):
    events_dic[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text,
    }

print(events_dic)

#driver.quit()


# driver.close - zamyka stronę
driver.quit() # - zamyka przeglądarkę - wszystkie storny / zakładki


