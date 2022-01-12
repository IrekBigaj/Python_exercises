# #100days of code - day 48-49 - Selenium Driver
# Important data are stored in config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\_Web\ChromeDriver\chromedriver.exe"

serv = Service(CHROME_DRIVER_PATH)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=opt)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

no = driver.find_element(By.CSS_SELECTOR, "#articlecount a")  # najpierw znajduje element articlecount a w nim element a
print(no.text)

#no.click()

all_portals = driver.find_element(By.LINK_TEXT, "All portals")  # Wyszukuje po treści linku wyświetlanej na stronie
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")  # Wpisuje wartości zamiast kalwiatury
search.send_keys(Keys.ENTER)  # Wciska znak Enter - są też inne możliwe

# driver.quit()
