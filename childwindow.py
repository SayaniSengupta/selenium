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
driver.get("https://the-internet.herokuapp.com/windows")
action = ActionChains(driver)
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()

#switch to new window
windowsopen = driver.window_handles
driver.switch_to.window(windowsopen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsopen[0])
assert "Opening a new window" == (driver.find_element(By.TAG_NAME, "h3").text)

