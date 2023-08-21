from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import string
import random
from functions import send_random_search, clear_search, sign_in

username = "xxx"
password = "xxx"

def search(driver, iterations, device):
    sign_in(driver, 10, username, password)
    bing_window = driver.current_window_handle
    driver.get("https://bing.com/")

    driver.switch_to.new_window('pointsbreakdown')
    points_window = driver.current_window_handle
    driver.get("https://rewards.bing.com/pointsbreakdown")

    points_xpath = ""

    if device == "desktop":
        points_xpath = "//*[@id='userPointsBreakdown']/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b"
    elif device == "mobile":
        points_xpath = "//*[@id='userPointsBreakdown']/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b"
    
    count = int(driver.find_element(By.XPATH, points_xpath).text)

    while ((count/5) - iterations != 0) :
        try:
            driver.switch_to.window(bing_window)
            random_search = ''.join(random.choices(string.ascii_letters + " ", k=random.randint(3, 15)))
            print(str(((count/5) - iterations)) + ": " + random_search)

            send_random_search(driver, 20, random_search, "//textarea[@type='search']")
            #time.sleep(0.5)
            clear_search(driver, 20, "//textarea[@type='search']")
            #time.sleep(0.5)

            driver.switch_to.window(points_window)
            #time.sleep(0.5)
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, points_xpath)))
            count = int(driver.find_element(By.XPATH, points_xpath).text)
        except:
            print("Uh oh!")
            time.sleep(2)

def desktop_search():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    search(driver, 30, "desktop")
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
    search(driver, 20, "mobile")
    driver.quit()