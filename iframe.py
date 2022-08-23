import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


name = "sayani"

service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("i am sayani")
driver.switch_to.default_content()
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element(By.TAG_NAME, "h3").text










