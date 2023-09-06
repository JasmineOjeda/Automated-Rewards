from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from functions import send_random_search, clear_search, get_random_search, alter_search

def desktop_search(driver):
    driver.maximize_window()
    search(driver, 30, "desktop")

def mobile_search(driver):
    driver.set_window_size(300, 600)
    search(driver, 20, "mobile")

def search(driver, iterations, device):
    action = ActionChains(driver)
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
    
    random_search = get_random_search()
    while ((count/5) - iterations != 0) :
        try:
            driver.switch_to.window(bing_window)
            action.move_to_element(driver.find_element(By.XPATH, "//textarea[@type='search']")).perform() #.click(hidden_submenu).perform()
            print(str(((count/5) - iterations)) + ": " + random_search)

            time.sleep(random.uniform(0.5, 1))
            send_random_search(driver, 20, random_search, "//textarea[@type='search']")
            time.sleep(0.5)
            clear_search(driver, 20, "//textarea[@type='search']")
            time.sleep(0.5)

            if (len(random_search) > 1):
                random_search = alter_search(random_search)
            else:
                random_search = get_random_search()
            
            driver.switch_to.window(points_window)
            #time.sleep(0.5)
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, points_xpath)))
            count = int(driver.find_element(By.XPATH, points_xpath).text)
        except:
            print("Uh oh!")
            time.sleep(2)
