from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

video = driver.find_element(by=By.ID, value="video-title")
video.click()

time.sleep(20)

