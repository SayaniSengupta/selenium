import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
name = "sayani"
#checkbox
service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
driver.implicitly_wait(5)
driver.maximize_window()
# action.drag_and_drop()
# action.double_click(driver.find_element(BY.))
action.click_and_hold()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.   context_click(driver.find_element(By.XPATH, "//a[text()='Reload']")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
