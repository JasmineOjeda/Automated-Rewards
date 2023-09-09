from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random as ran

# * * * * * STRING FUNCTIONS * * * * *
def alter_search(search_text):
    length = len(search_text)
    changed_search = search_text.replace(" ", "", ran.randint(0, 1))

    if (length > 1):
        index = ran.randint(0, length - 1)
        changed_search = changed_search[:index] + "" + changed_search[index + 1:]

    return changed_search

def get_random_search():
    search_text = ""
    
    event = ran.choice(open("src\dictionary\events.txt").read().split(", "))
    job = ran.choice(open("src\dictionary\jobs.txt").read().split(", "))
    noun = ran.choice(open("src\dictionary\\nouns.txt").read().split(", "))
    proper_noun = ran.choice(open("src\dictionary\proper_nouns.txt").read().split(", "))
    question = ran.choice(open("src\dictionary\questions.txt").read().split(", "))
    verb = ran.choice(open("src\dictionary\\verbs.txt").read().split(", "))

    topic = ran.randint(0, 2)

    if (topic == 0): # Create "question" search text
        if (question != "how to become"):
            search_text = question + " " + ran.choice(["", verb + " "]) + ran.choice(["", proper_noun + " "]) + noun
        else:
            search_text = question + " " + ran.choice(["", proper_noun + " ", event + " "]) + job
    elif (topic == 1): # Create "shopping" search text
        search_text = ran.choice(["", proper_noun + " "]) + noun
    else: # Create "random" search text
        tmp1 = ran.choice(["", proper_noun + " "]) + noun + ran.choice(["", event + " "])
        tmp2 = job + " " + verb + " " + event
        search_text = ran.choice([tmp1, tmp2])
    
    # Random wait
    time.sleep(ran.uniform(0.5, 3.5))
    return search_text

# * * * * * DRIVER FUNCTIONS * * * * *
def send_random_search(driver, timeout, string, xpath):
    print("\tSending " + string + " . . .")
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).send_keys(string + "\n")
    print("\tSent!")

def clear_search(driver, timeout, xpath):
    print("\tErasing . . .")
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).clear()
    print("\tErased!")

def sign_in(driver, timeout, username, password):
    driver.get("https://login.live.com/")
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(username)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@id='i0118']")))
        driver.find_element(By.XPATH, "//*[@id='i0118']").send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
        time.sleep(2)
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@id='KmsiCheckboxField']")))
        driver.find_element(By.XPATH, "//*[@id='KmsiCheckboxField']").click()
        driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
    except:
        print("Already logged in!")

