import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pickle
import time
import sys

sys.path.insert(1, 'src')
import search
import activities
import functions

username = "xxx"
password = "xxx"

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True   
edge_options.add_argument("start-maximized")
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_argument("--user-data-dir=C:\\path\\to\\user data")
edge_options.binary_location = r"C:\path\to\\msedge.exe"
mobile_emulation = {  
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 }, 
        "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"  
    } 

edge_options.add_experimental_option("mobileEmulation", mobile_emulation)

serv = Service("msedgedriver.exe")
driver = webdriver.Edge(service=serv, options=edge_options)
time.sleep(3)

# SIGN INTO ACCOUNT IF NEEDED
functions.sign_in(driver, 10, username, password)
# PERFORM MOBILE SEARCH
search.mobile_search(driver)
# RESET OPTIONS TO DESKTOP
time.sleep(3)
driver.quit()
edge_options.add_experimental_option("mobileEmulation", {})
driver = webdriver.Edge(service=serv, options=edge_options)
# PERFORM DESKTOP SEARCH
search.desktop_search(driver)
#activities.perform_activites(driver)

# TEST FOR BOT DETECTION
# Credit: https://medium.com/@molixnu/avoiding-bot-detection-with-selenium-python-bypassing-puzzle-captcha-using-a-cookie-based-dd1e95965b37
#driver.get("https://www.idealista.com/")
#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)
#driver.get("https://www.idealista.com/")

time.sleep(3)
driver.quit()
    