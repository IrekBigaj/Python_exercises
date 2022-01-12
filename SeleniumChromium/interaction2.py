# #100days of code - day 48-49 - Selenium Driver
# Important data are stored in config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

CHROME_DRIVER_PATH = "C:\_Web\ChromeDriver\chromedriver.exe"

serv = Service(CHROME_DRIVER_PATH)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=opt)

driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Python_Master")  # Wpisuje wartości zamiast kalwiatury

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Super Hero")

email = driver.find_element(By.NAME, 'email')
email.send_keys("i@i.pl")

# button = driver.find_element(By.CLASS_NAME, "btn")
button = driver.find_element(By.CSS_SELECTOR, "form button") # inna metoda na znalezienie przyciski
button.click()

# switch to new window
#driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')  # to open TAB

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')  # to open TAB  - nie działa

driver.execute_script('''window.open("http://stackoverflow.com/", "_blank");''')  # other method to open TAB

driver.switch_to.window(driver.window_handles[1])
sleep(1)
print(driver.title)
driver.switch_to.window(driver.window_handles[0])

print(driver.title)
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')  # to close TAB - nie działa
driver.close()



# driver.quit()
