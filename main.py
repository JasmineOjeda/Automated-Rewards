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
edge_options.add_argument("user-data-dir=path to user data")
edge_options.add_argument("profile-directory=Profile 1")
edge_options.binary_location = r"path to msedge.exe"
#–disable-notifications

serv = Service("msedgedriver.exe")
driver = webdriver.Edge(service=serv, options=edge_options)
print("Opened window")

driver.get("https://www.idealista.com/")

#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)

#driver.get("https://www.idealista.com/")

#print(functions.get_random_search())

#search.desktop_search()
#search.mobile_search()
#activities.perform_activites(driver)

time.sleep(5)
driver.quit()
    