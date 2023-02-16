from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

search_input = driver.find_element(by=By.NAME, value="search_query")
search_input.send_keys("лідія шкварла dance clip")

time.sleep(3)

button_search = driver.find_element(by=By.ID, value="search-icon-legacy")
button_search.click()

time.sleep(3)

video = driver.find_element(by=By.ID, value="title-wrapper")
video.click()

time.sleep(120)

