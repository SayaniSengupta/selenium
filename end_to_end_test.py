from multiprocessing.connection import wait
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#checkbox+

service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
x = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for y in x:
   name = y.find_element(By.XPATH, "div/h4/a").text
   print(name)
   if name == "Blackberry":

    y.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
x = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in x




