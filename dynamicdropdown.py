import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
choice = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(choice))
for country in choice:
    if country.text=="India":
        country.click()
        break
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
