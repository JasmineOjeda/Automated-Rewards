from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random

def daily_set(driver):
    driver.get("https://rewards.bing.com/")
    rewards_window = driver.current_window_handle
    count = 3
    card_number = 1

    while(count > 0):
        card = "//*[@id='daily-sets']/mee-card-group[1]/div/mee-card[" + str(card_number) + "]/div/card-content/mee-rewards-daily-set-item-content"
        try:
            driver.find_element(By.XPATH, card).click()
            count -= 1
            card_number += 1
        except:
            time.sleep(2)
    

    windows = driver.window_handles

    for window in windows:
        if(window != rewards_window):
            driver.switch_to.window(window)
            ifQuiz(driver)
            ifPoll(driver)
            driver.close()

    driver.switch_to.window(rewards_window)

def ifQuiz(driver):
    try:
        try:
            driver.find_element(By.XPATH, "//*[@id='rqStartQuiz']")
        except NoSuchElementException:
            print("There is no start button")

        count = 0
        number = driver.find_element(By.XPATH, "//*[@id='QuestionPane" + str(count) + "']/div[2]").text
        total = int(number[6])

        while count < total:
            try:
                print("\tQuestion " + str(count + 1))
                driver.find_element(By.XPATH, "//*[@id='QuestionPane" + str(count) + "']/div[1]/div[2]/a[" + str(random.randint(1, 3)) + "]").click()
                if count < (total - 1):
                    driver.find_element(By.XPATH, "//*[@id='nextQuestionbtn" + str(count) + "']").click()
                count += 1
            except:
                time.sleep(2)
    except NoSuchElementException:
        print("Not a quiz")

def ifPoll(driver):
    try:
        driver.find_element(By.XPATH, "//*[@id='btoption" + str(random.randint(0, 1)) + "']").click()
    except NoSuchElementException:
        print("Not a poll")
