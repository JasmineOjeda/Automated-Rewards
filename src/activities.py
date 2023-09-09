from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random

#plus icon (first card): for needs to be done
# //*[@id="more-activities"]/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/mee-rewards-points/div/div/span[1]
# <span class="mee-icon mee-icon-AddMedium" ng-if="$ctrl.iconName" aria-label="plus" role="note"></span>

# checkmark icon (thrid card): for completed
# //*[@id="more-activities"]/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/mee-rewards-points/div/div/span[1]
# <span class="mee-icon mee-icon-SkypeCircleCheck" ng-if="$ctrl.iconName" aria-label="plus" role="note"></span>

def perform_activites(driver):
    # Daily Set
    #set(driver, 3, "//*[@id='daily-sets']/mee-card-group[1]/div/mee-card[", "]/div/card-content/mee-rewards-daily-set-item-content")
    # More Activites
    set(driver, 15, "//*[@id='more-activities']/div/mee-card[", "]/div/card-content/mee-rewards-more-activities-card-item/div/a")

def set(driver, total, card_first, card_last):
    driver.get("https://rewards.bing.com/")
    rewards_window = driver.current_window_handle
    card_number = 1
    card_set = []

    while(total >= card_number):
        print("Card " + str(card_number))
        card_xpath = card_first + str(card_number) + card_last
        
        try:
            try:
                driver.find_element(By.XPATH, card_xpath).find_element(By.XPATH, "//span[@class='mee-icon mee-icon-AddMedium']")
                card_set.append(driver.find_element(By.XPATH, card_xpath))
            except:
                print("\tN/A for points")
            card_number += 1
        except:
            time.sleep(2)
            print("Oops")

    for card in card_set:
        card.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(random.uniform(1.0, 3.5))
        ifQuiz(driver)
        ifPoll(driver)
        print("\n")
        driver.close()
        driver.switch_to.window(rewards_window)
        time.sleep(0.5)

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
                #time.sleep(0.5)
                cur_points = int(driver.find_element(By.XPATH, "//*[@id='btoHeadPanel']/span[3]/span[2]/span[1]/span[1]/span").text)
                option = 0

                while cur_points == count:
                    print("\t\tTrying option " + str(option + 1) + ". . .")
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
                #time.sleep(0.5)
                print("\tQuestion " + str(count + 1))
                driver.find_element(By.XPATH, "//*[@id='QuestionPane" + str(count) + "']/div[1]/div[2]/a[" + str(random.randint(1, 3)) + "]").click()
                if count < (int(total) - 1):
                    time.sleep(0.5)
                    driver.find_element(By.XPATH, "//*[@id='nextQuestionbtn" + str(count) + "']").click()
                count += 1
            except:
                print("Pending...")
                time.sleep(2)
    except:
        print("Not a weekly quiz")

def ifPoll(driver):
    try:
        driver.find_element(By.XPATH, "//*[@id='btoption" + str(random.randint(0, 1)) + "']").click()
    except NoSuchElementException:
        print("Not a poll")
