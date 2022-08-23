import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
#checkbox
service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
choice = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for ch in choice:
    if ch.get_attribute("value")=="option2":
        ch.click()
        assert ch.is_selected()
        break

# choice1 = driver.find_elements(By.XPATH, "//input[@type='radio']")
# for select in choice1:
#     if select.get_attribute("value") == "radio1":
#         select.click()
#         assert select.is_selected()
#         break
#radiobutton

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#display box

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()








