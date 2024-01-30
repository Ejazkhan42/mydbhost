import pytest

from Helper.packages.requirments import (
    setup_driver as driver,
    xpath_click_Xpath as XapthClick,
    dropdownEnter as dropText,
    dropdownXapth as dropXath,
    enter_text_xpath as XapthText,
    enter_text_clear_input_Xpath as ClearTexTXapth,
    Candates_DataSet,
    Base_Url,
    visibility,
    getTextValue,
)

from Helper.objects.LoginObjects import login, Home, Candidates
import subprocess


@pytest.fixture
def Login_without_SSO(test_driver):
    Login = Base_Url()
    driver = test_driver
    # driver.maximize_window()
    Candidate_Data = Candates_DataSet()
    for x in range(0, len(Login['UserName'])):
        base_url = Login['Base_Url'][x]
        driver.get(base_url)
        if driver.title == "Sign In":
            UserName = Login['UserName'][x]
            Password = Login['Password'][x]
            ClearTexTXapth(driver, login.username_xapth(), UserName)
            ClearTexTXapth(driver, login.password_xapth(), Password)
            XapthClick(driver, login.loginButton())
        else:
            pass
    Welcome(driver)
    for x in range(0, len(Candidate_Data)):
        First = Candidate_Data["Fname"][x]
        Last = Candidate_Data["Lname"][x]
        Email = Candidate_Data["Email"][x]
        Candates_Add(driver, First, Last, Email)
    driver.quit()

def Welcome(driver):
    step_marker("Step 1 Clicking Home_Button", driver)
    XapthClick(driver, Home.Home_Button())
    step_marker("Step 2 Clicking MyClient_Group", driver)
    XapthClick(driver, Home.MyClient_Group())
    step_marker("Step 3 Clicking Hiring_Tab", driver)
    XapthClick(driver, Home.Hiring_Tab())

def Candates_Add(driver, FirstName, LastName, Email):
    step_marker("Step 4 Clicking Candidates_Tab", driver)
    XapthClick(driver, Candidates.Candidates_Tab())
    step_marker("Step 5 Clicking Search_Candidates_Button", driver)
    XapthClick(driver, Candidates.Search_Candidates_Button())
    step_marker("Step 6 Clicking add_button", driver)
    XapthClick(driver, Candidates.add_button())
    step_marker("Step 7 Typing First Name", driver)
    XapthText(driver, Candidates.FirstName_Input(), FirstName)
    step_marker("Step 8 Typing Last Name", driver)
    XapthText(driver, Candidates.LastName_Input(), LastName)
    # XapthText(driver, Candidates.Email_Input(), Email)
    step_marker("Step 9 Clicking Save_and_close_button", driver)
    XapthClick(driver, Candidates.Save_and_close_button())
    step_marker("Step 10 Clicking Yes_button", driver)
    XapthClick(driver, Candidates.Yes_button())
    step_marker("Step 11 Clicking Done_Button", driver)
    XapthClick(driver, Candidates.Done_Button())
    number = getTextValue(driver, Candidates.CandidatesNumber())
    visibility(driver, Candidates.add_button())
    step_marker("Step 12 Clicking Done_Button Again", driver)
    XapthClick(driver, Candidates.Done_Button())

# Mark a step in the report with screenshot

def step_marker(message, driver):
    pytest.mark.step(message)
    outcome = yield
    report = outcome.get_result()

# Test function using the fixture
@pytest.mark.login
def test_login_without_sso(Login_without_SSO):
    pass  # Your actual test code goes here

