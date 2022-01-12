# #100days of code - day 48-49 - Selenium Driver
# Important data are stored in config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from time import *

CHROME_DRIVER_PATH = "C:\_Web\ChromeDriver\chromedriver.exe"

serv = Service(CHROME_DRIVER_PATH)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=opt)


driver.get("https://www.linkedin.com/uas/login")

sleep(1)

login = driver.find_element(By.ID, "username")
login.send_keys(MY_EMAIL)
pswd = driver.find_element(By.ID, "password")
pswd.send_keys(LI_PASSWORD)

button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

# button = driver.find_element(By.CLASS_NAME, "btn__primary--large from__button--floating")
button.click()

sleep(5)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2&keywords=Python&sortBy=R")
adv_list_name = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list a")
# adv_list_name = driver.find_elements(By.CSS_SELECTOR, ".jobs-card-list a")

for n in range(0, 1):  # , len(adv_list_name)):
    print(adv_list_name[n].text)
    link = adv_list_name[n].get_attribute("href")
    print(link)
    driver.get(link)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()


