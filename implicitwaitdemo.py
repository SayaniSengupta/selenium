import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("sayani")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='promoInfo']").text


