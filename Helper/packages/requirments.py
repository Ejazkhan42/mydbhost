#Helper Functions
import json
import subprocess
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import re
import datetime
import pandas as p
secs=10
username = "karaechi420"  # Replace the username
access_key ="fhnYMqQ4ClncMZjcBWZQQkYq6YlBvNfsa9SEjRhyUsFxE3SSgS"  # Replace the access key

def setup_driver(set,browser="Edge"):

    if set==1 and browser=="Chrome":
    
        options = ChromeOptions()
        options.browser_version = "latest"
        options.platform_name = "win10"
        lt_options = {}
        lt_options["username"] = username
        lt_options["accessKey"] = access_key
        lt_options["video"] = True
        lt_options["resolution"] = "1920x1080"
        lt_options["network"] = True
        lt_options["build"] = "test_build"
        lt_options["project"] = "unit_testing"
        lt_options["smartUI.project"] = "test"
        lt_options["name"] = "basic_unit_selinium"
        lt_options["w3c"] = True
        lt_options["plugin"] = "python-python"
        options.set_capability("LT:Options", lt_options)
        driver = webdriver.Remote(
                command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                    username, access_key
                ),
                options=options,
            )
        return driver
    elif set==2 and browser=="Edge":
        options = webdriver.EdgeOptions()
        driver=webdriver.Edge(options=options)
        return driver
    elif set==3 and browser=="Firfox":
        options=webdriver.FirefoxOptions()
        driver=webdriver.Edge(options=options)
        return driver
    elif set==0 and browser=="Edge":
        options = ChromeOptions()
        options.set_capability('sessionName', 'BStack Sample Test')
        driver = webdriver.Chrome(options=options)
        return driver


def xpath_click_Xpath(driver, xpath,post=-1):
    try:
        clicked_flag = getattr(driver, f"{xpath}_clicked", False)
        if not clicked_flag:
            wait = WebDriverWait(driver, secs)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            highlight(driver,element, 3, "red", 5)
            element.click()
            if post > 0:
                driver.implicitly_wait(post)

            setattr(driver, f"{xpath}_clicked", True)
    except TimeoutException:
        print(f"Timeout waiting for element with XPath '{xpath}' to be clickable.")


def highlight(driver,element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

def enter_text_xpath(driver, xpath, text,post=-1):
    wait = WebDriverWait(driver, secs)
    try:
        clicked_flag = getattr(driver, f"{xpath}_clicked", False)
        if not clicked_flag:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            highlight(driver, element, 3, "red", 5)
            element.send_keys(text)
            if post > 0:
                driver.implicitly_wait(post)
            setattr(driver, f"{xpath}_clicked", True)
    except TimeoutException:
        print(f"Timeout waiting for element with XPath '{xpath}' to be clickable.")


def dropdownXapth(driver, xpath, num=0,post=-1):
    try:
        clicked_flag = getattr(driver, f"{xpath}_clicked", False)
        if not clicked_flag:
            wait = WebDriverWait(driver, secs)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            highlight(driver, element[num], 3, "red", 5)
            element[num].click()
            if post > 0:
                driver.implicitly_wait(post)
            setattr(driver, f"{xpath}_clicked", True)
    except TimeoutException:
        print(f"Timeout waiting for element with XPath '{xpath}' to be clickable.")
        


def dropdownEnter(driver, xpath, text, num=0,post=-1):
    try:
        clicked_flag = getattr(driver, f"{xpath}_clicked", False)
        if not clicked_flag: 
            wait = WebDriverWait(driver, secs)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            highlight(driver, element[num], 3, "red", 5)
            element[num].clear()
            element[num].send_keys(text)
            if post > 0:
                driver.implicitly_wait(post)
            setattr(driver, f"{xpath}_clicked", True)
    except TimeoutException:
        print(f"Timeout waiting for element with XPath '{xpath}' to be clickable.")


def enter_text_clear_input_Xpath(driver, xpath, text,post=-1):
    try:
        clicked_flag = getattr(driver, f"{xpath}_clicked", False)
        if not clicked_flag:
            wait = WebDriverWait(driver, secs)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            highlight(driver, element, 3, "red", 5)
            element.send_keys(text)
            if post > 0:
                driver.implicitly_wait(post)
            setattr(driver, f"{xpath}_clicked", True)
    except TimeoutException:
        print(f"Timeout waiting for element with XPath '{xpath}' to be clickable.")

def Candates_DataSet():
    Candidates = p.read_excel('./Helper/DataSet/Data.xlsx', 'Candidates')
    return Candidates


def Base_Url():
    Url = p.read_excel('./Helper/DataSet/Data.xlsx', 'Login')
    return Url


def visibility(driver,xpath):
    wait = WebDriverWait(driver, secs)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

def Requisition():
    Requisition=p.read_excel('./Helper/DataSet/Data.xlsx','Requistion')
    return Requisition

def getTextValue(driver,xpath):
    wait = WebDriverWait(driver, secs)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    print(element.text)
    return number(element.text)

def number(text):
    regex = r'([0-9])\w+'
    test_str = (f"{text}\n")

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches, start=1):
        numbers=match.group()
        return numbers




def RType(Type):
    # Requisition Type
    if Type=="Standard":
        return 0
    elif Type=="Pipeline":
        return 1    
    # Use Input
    elif Type=="Template":
        return 0
    elif Type=="Position":
        return 1
    elif Type=="Job":
        return 2
    elif Type=="Existing Requisition":
        return 3
    elif Type=="Blank Requisition":
        return 4
    # Requiting Types
    elif Type=="Campus":
        return 0
    elif Type=="Contingent":
        return 1
    elif Type=="Executive":
        return 2
    elif Type=="Hourly":
        return 3
    elif Type=="Professional":
        return 4
    #Worker Types
    elif Type=="Contingent worker":
        return 0
    elif Type=="Employee":
        return 1  
    #Full or Partime Input
    elif Type=="Full time":
        return 0
    elif Type=="Part time":
        return 1
    # Regular or Temporary Input
    elif Type=="Regular":
        return 0
    elif Type=="Temporary":
        return 1
    #Travel Yes and No
    elif Type=="Yes":
        return 0
    elif Type=="No":
        return 1
    # Work Place
    elif Type=="On-site":
        return 0
    elif Type=="Hybrid":
        return 1
    elif Type=="Remote":
        return 2

