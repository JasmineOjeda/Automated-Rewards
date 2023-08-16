from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
sys.path.insert(1, 'src')
import search
import activities

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

search.desktop_search()
search.mobile_search()
activities.daily_set(driver)

time.sleep(3)
driver.quit()
    