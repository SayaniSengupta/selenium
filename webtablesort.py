import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
#checkbox
service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
veggilist = []
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
list = driver.find_elements(By.XPATH, "//tr/td[1]")
for l in list:
    print(l.text)
    veggilist.append(l.text)
    browsersortedveggilist = veggilist.copy()
veggilist.sort()

assert browsersortedveggilist == veggilist

