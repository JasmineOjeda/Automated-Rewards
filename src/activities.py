from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import random

def perform_activites(driver):
    # Daily Set
    set(driver, "//*[@id='daily-sets']/mee-card-group[1]/div", ".//mee-rewards-daily-set-item-content")
    # More Activites
    set(driver, "//*[@id='more-activities']/div", ".//mee-rewards-more-activities-card-item")

def set(driver, container_xpath, card_xpath):
    driver.get("https://rewards.bing.com/")
    rewards_window = driver.current_window_handle
    card_set = driver.find_element(By.XPATH, container_xpath).find_elements(By.XPATH, card_xpath)


    while(len(card_set) > 0):
        cards_to_remove = []
        print("Before: " + str(len(card_set)))

        for card in card_set:
            try:
                card.find_element(By.XPATH, ".//*[@class='mee-icon mee-icon-AddMedium']")
            except NoSuchElementException:
                print("Removing N/A card...")
                cards_to_remove.append(card)

        for card in cards_to_remove:
            card_set.remove(card)

        print("After: " + str(len(card_set)))
        cards_to_remove = []
        count = 1

        for card in card_set:
            print("Card " + str(count))
            try:
                card.click()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(random.uniform(1.0, 3.5))
                ifQuiz(driver)
                ifPoll(driver)
                print("\n")
                driver.close()
                driver.switch_to.window(rewards_window)
                time.sleep(0.5)
            except ElementNotInteractableException:
                print("\tNot clickable card")
            count += 1

    driver.switch_to.window(rewards_window)

def ifQuiz(driver):
    try:
        time.sleep(0.5)
        try:
            driver.find_element(By.XPATH, "//*[@id='8B0C5D_43_btn']").click()
        except:
            print("Start button container not found...")

        try:
            driver.find_element(By.XPATH, "//*[@id='rqStartQuiz']").click()
        except NoSuchElementException:
            print("...there is no start button")

        ifWeeklyQuiz(driver)
        ifWarpQuiz(driver)
        ifTurboQuiz(driver)

    except NoSuchElementException:
        print("Not a quiz")

def ifTurboQuiz(driver):
    try:
        current = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[2]/span[1]/span").text)
        total = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[2]/span[2]").text)
        count = 0

        while (current * 10) < total:
            try:
                print("\tQuestion " + str(count + 1), " " + str(current * 10) + " / " + str(total))
                driver.find_element(By.XPATH, "//*[@id='rqAnswerOption" + str(random.randint(0, 2)) + "']").click()
                cur_points = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[2]/span[1]/span").text)
                option = 0
   
                while cur_points == (count * 10):
                    print("\t\tTrying option " + str(option + 1) + ". . .")
                    time.sleep(random.uniform(0.5, 1.5))
                    driver.find_element(By.XPATH, "//*[@id='rqAnswerOption" + str(option) + "']").click()
                    option += 1
                    cur_points = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[2]/span[1]/span").text)
                
                count = cur_points / 10
            except:
                print("Pending...")
                time.sleep(2)
    except:
        print("Not a turbo quiz")

def ifWarpQuiz(driver):
    try:
        count = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[1]/span[1]/span").text)
        total = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[1]/span[2]").text)

        while count < total:
            try:
                print("\t" + str(count) + " out of " + str(total))
                time.sleep(0.5)
                cur_points = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[1]/span[1]/span").text)
                option = 0

                while cur_points == count:
                    print("\t\tTrying option " + str(option + 1) + ". . .")
                    time.sleep(random.uniform(0.5, 1.5))
                    driver.find_element(By.XPATH, "//*[@id='rqAnswerOption" + str(option) + "']").click()
                    option += 1
                    cur_points = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[1]/span[1]/span").text)
                
                count = cur_points
            except:
                print("Pending...")
                time.sleep(2)
    except:
        print("Not a warp quiz")

def ifWeeklyQuiz(driver):
    try:
        count = 0
        total = driver.find_element(By.XPATH, "//*[@id='QuestionPane" + str(count) + "']/div[2]").text
        total = total.split()[2]
        total = total.rstrip(total[-1])

        while count < int(total):
            try:
                time.sleep(0.5)
                print("\tQuestion " + str(count + 1))
                time.sleep(random.uniform(0.5, 1.5))
                driver.find_element(By.XPATH, "//*[@id='QuestionPane" + str(count) + "']/div[1]/div[2]/a[" + str(random.randint(1, 3)) + "]").click()
                if count < (int(total) - 1):
                    time.sleep(1)
                    driver.find_element(By.XPATH, "//*[@id='nextQuestionbtn" + str(count) + "']").click()
                count += 1
            except:
                print("Pending...")
                time.sleep(2)
    except:
        print("Not a weekly quiz")

def ifPoll(driver):
    try:
        time.sleep(random.uniform(0.5, 1.5))
        driver.find_element(By.XPATH, "//*[@id='btoption" + str(random.randint(0, 1)) + "']").click()
        time.sleep(3)
    except NoSuchElementException:
        print("Not a poll")
