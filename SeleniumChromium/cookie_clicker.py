# #100days of code - day 48-49 - Selenium Driver
# Important data are stored in config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\_Web\ChromeDriver\chromedriver.exe"

serv = Service(CHROME_DRIVER_PATH)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=opt)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

#cursor_price = driver.find_element(By.CSS_SELECTOR, '#rightPanel #store #buyCursor b .amount')


five_min = 5*60   # [seconds]
timeout_check = 3   # [seconds]
five_min_start = time.time()
timeout = time.time() + timeout_check

while time.time() < five_min_start + five_min:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    if time.time() > timeout:

        money = driver.find_element(By.ID, "money").text.replace(",", "")
        money_int = int(money)
        # print(money)

        cursor_price = driver.find_element(By.CSS_SELECTOR, '#rightPanel #store #buyCursor b')
        cursor_price_int = int(cursor_price.text.replace(" ", "").replace(",", "").split("-")[1])
        grandma = driver.find_element(By.ID, "buyGrandma")
        grandma_price = driver.find_element(By.CSS_SELECTOR, '#rightPanel #store #buyGrandma b')
        grandma_price_int = int(grandma_price.text.replace(" ", "").replace(",", "").split("-")[1])
        factory = driver.find_element(By.ID, "buyFactory")
        factory_price = driver.find_element(By.CSS_SELECTOR, '#rightPanel #store #buyFactory b')
        factory_price_int = int(factory_price.text.replace(" ", "").replace(",", "").split("-")[1])
        mine = driver.find_element(By.ID, "buyMine")
        mine_price = driver.find_element(By.CSS_SELECTOR, '#rightPanel #store #buyMine b')
        mine_price_int = int(mine_price.text.replace(" ", "").replace(",", "").split("-")[1])

        if money_int >= mine_price_int:
            mine.click()
        else:
            if money_int >= factory_price_int:
                factory.click()
            else:
                if money_int >= grandma_price_int:
                    grandma.click()
                else:
                    if money_int >= cursor_price_int:
                        cursor = driver.find_element(By.ID, "buyCursor")
                        cursor.click()

        timeout = time.time() + 5

cookie_per_s = driver.find_element(By.ID, "cps").text
print(cookie_per_s)
driver.quit()
