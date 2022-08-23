from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/home/user/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("sayani.png")
