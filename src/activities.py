from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def daily_set(driver):
    driver.get("https://rewards.bing.com/")
    count = 3
    card_number = 1
    time.sleep(5)

    while(count > 0):
        card = "//*[@id='daily-sets']/mee-card-group[1]/div/mee-card[" + str(card_number) + "]/div/card-content/mee-rewards-daily-set-item-content"
        time.sleep(2)
        driver.find_element(By.XPATH, card).click()
        time.sleep(2)
        driver.get("https://rewards.bing.com/")
        count -= 1
        card_number += 1