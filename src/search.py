from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random
from functions import send_random_search, clear_search

def search(driver, iterations):
    driver.get("https://bing.com/")
    time.sleep(5)
    count = iterations

    while (count > 0) :
        try:
            random_search = ''.join(random.choices(string.ascii_letters + " ", k=random.randint(3, 15)))
            print(str(count) + ": " + random_search)
            send_random_search(driver, 20, random_search, "//textarea[@type='search']")
            time.sleep(0.5)
            clear_search(driver, 20, "//textarea[@type='search']")
            time.sleep(0.5)
            count -= 1
        except:
            time.sleep(5)

def desktop_search():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    search(driver, 30)
    driver.quit()

def mobile_search():
    options = webdriver.EdgeOptions()
    #options.use_chromium = True  
    
    mobile_emulation = {  
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },  
        "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"  
    }  
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Edge(options=options)
    search(driver, 20)
    driver.quit()