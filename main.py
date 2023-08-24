from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
sys.path.insert(1, 'src')
import search
import activities
import functions

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

#print(functions.get_random_search())
search.desktop_search()
search.mobile_search()
activities.perform_activites(driver)

time.sleep(3)
driver.quit()
    