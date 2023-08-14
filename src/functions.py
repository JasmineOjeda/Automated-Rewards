from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def send_random_search(driver, timeout, string, xpath):
    print("\tSending " + string)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    print("\tSending. . .")
    driver.find_element(By.XPATH, xpath).send_keys(string + "\n")
    print("\tSent!")

def clear_search(driver, timeout, xpath):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    print("\tErasing . . .")
    driver.find_element(By.XPATH, xpath).clear()
    print("\tErased!")
