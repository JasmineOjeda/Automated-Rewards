from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

def search(driver, iterations):
    driver.get("https://bing.com/")
    time.sleep(3)
    count = iterations

    while (count > 0) :
        random_search = ''.join(random.choices(string.ascii_letters + " ", k=random.randint(3, 15)))
        print(str(count) + ": " + random_search)
        driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys(random_search)
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys("\n")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[type='search']").clear()
        time.sleep(0.5)
        count -= 1

def desktop_search():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    search(driver, 30)
    driver.quit()

def mobile_search():
    options = webdriver.EdgeOptions()
    options.use_chromium = True  
    
    mobile_emulation = {  
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },  
        "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"  
    }  
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Edge(options=options)
    search(driver, 20)
    driver.quit()

desktop_search()
mobile_search()

#driver.get("https://rewards.bing.com/")
    