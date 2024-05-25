from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
from pathlib import Path
import winreg

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.skill-capped.com/valorant/browse/course/0rrxwlwsdd/0rhxtnrc3q")
try:
    course = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/div[7]/div/div/div[3]/div[1]/div[1]/div/div[1]"))
     )
finally:
     course.click()
time.sleep(4)
ahmet = 'BrVidRow-0rrxwlwsdd'
print(driver.find_element(By.XPATH,f"//*[@id='{ahmet}']/div/div[1]/div[2]/div/div[1]").get_attribute("innerText"))
