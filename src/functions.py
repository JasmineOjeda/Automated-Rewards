from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

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
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
    except:
        print("Already logged in!")