from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

driver.get("https://bing.com/")
time.sleep(3)

##driver.get("https://rewards.bing.com/")

count = 30

while (count > 0) :
    random_search = ''.join(random.choices(string.ascii_letters + " ", k=random.randint(3, 15))) + "\n"
    ##print(random_search)
    driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys(random_search)
    count-=1
    time.sleep(random.randint(1, 3))
    driver.find_element(By.CSS_SELECTOR, "[type='search']").clear()
    