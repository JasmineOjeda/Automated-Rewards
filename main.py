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

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True   
edge_options.add_argument("start-maximized")
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_argument("user-data-dir=path to User Data")
edge_options.add_argument("profile-directory=path to profile")
edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

serv = Service("msedgedriver.exe")
driver = webdriver.Edge(service=serv, options=edge_options)
time.sleep(2)
#print("Opened window")

# TEST FOR BOT DETECTION
#driver.get("https://www.idealista.com/")
#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)
#driver.get("https://www.idealista.com/")


#print(functions.get_random_search())

functions.sign_in(driver, 10, "xxx", "xxx")
#search.search(driver, 5, "desktop")
#search.desktop_search()
#search.mobile_search()
#activities.perform_activites(driver)

time.sleep(1000)
driver.quit()
    