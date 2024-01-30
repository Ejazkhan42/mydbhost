# Helper Functions
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import pandas as p


def setup_driver():
    options = webdriver.EdgeOptions()
    options.add_argument('user-data-dir=C:\\Users\\EJAZ\\AppData\\Local\\Microsoft\\Edge\\User Data')
    driver = webdriver.Edge(options=options)
    return driver
    # driver=webdriver.Chrome()
    # return driver


def xpath_click_Xpath(driver, xpath):
    wait = WebDriverWait(driver, secs)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


def enter_text_xpath(driver, xpath, text):
    wait = WebDriverWait(driver, secs)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(text)


def xpath_num_click_Xpath(driver, xpath, num=0):
    wait = WebDriverWait(driver, secs)
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    elements[num].click()


def enter_num_text_Xapth(driver, xpath, text, num=0):
    wait = WebDriverWait(driver, secs)
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    elements[num].clear()
    elements[num].send_keys(text)


def enter_text_clear_input_Xpath(driver, xpath, text):
    wait = WebDriverWait(driver, secs)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.clear()
    element.send_keys(text)


def How(driver, Type, Unit, Title, Use, index):
    # 1 How Tab
    print("Job Requisition How Tab Start")
    xpath_click_Xpath(driver, "//input[contains(@id,'reTySel::content')]")
    # Standard _adfiv='0' and pipeline _adfiv='1'
    xpath_click_Xpath(driver, f"//ul[@aria-label='Requisition Type']/li[@_adfiv='{Type}']")
    # Postions _adfiv='1' or Job _adfiv='2'
    # posIs::content position #jobIs::content job
    if Use == 1:
        xpath_click_Xpath(driver, "//input[contains(@id,'sourSel::content')]")
        xpath_click_Xpath(driver, f"//ul[@aria-label='Use']/li[@_adfiv='{Use}']")
        enter_text_clear_input_Xpath(driver, "//input[contains(@id,'buIs::content')]", Unit)
        xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
        enter_text_clear_input_Xpath(driver, "//input[contains(@id,'posIs::content')]", Title)
        xpath_click_Xpath(driver, f"//tr[@aria-rowindex='{index}']")
        xpath_click_Xpath(driver, "//button[contains(@id,'0:bicoBtn')]")
        print("Completed Tab")
    elif Use == 2:
        xpath_click_Xpath(driver, "//input[contains(@id,'sourSel::content')]")
        xpath_click_Xpath(driver, f"//ul[@aria-label='Use']/li[@_adfiv='{Use}']")
        enter_text_clear_input_Xpath(driver, "//input[contains(@id,'buIs::content')]", Unit)
        xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
        enter_text_clear_input_Xpath(driver, "//input[contains(@id,'jobIs::content')]", Title)
        xpath_click_Xpath(driver, f"//tr[@aria-rowindex='{index}']")
        xpath_click_Xpath(driver, "//button[contains(@id,'0:bicoBtn')]")
        print("Completed Tab")
    elif Use == 3:
        xpath_click_Xpath(driver, "//input[contains(@id,'sourSel::content')]")
        xpath_click_Xpath(driver, f"//ul[@aria-label='Use']/li[@_adfiv='{Use}']")
        enter_text_clear_input_Xpath(driver, "//input[contains(@id,'reqIs::content')]", Title)
        xpath_click_Xpath(driver, f"//tr[@aria-rowindex='{index}']")
        xpath_click_Xpath(driver, "//button[contains(@id,'0:bicoBtn')]")
        print("Completed Tab")
    else:
        xpath_click_Xpath(driver, "//button[contains(@id,'0:bicoBtn')]")
        print("Completed Tab")


def Basic(driver, job, limit, N):
    print("Job Requisition Basic Info Tab Start")
    enter_text_xpath(driver, "//input[contains(@id,'juseSel::content')]", job)
    if limit == "Limited":
        enter_text_xpath(driver, "//input[@title='Limited']", limit)
        enter_text_clear_input_Xpath(driver, f"//input[contains(@id,'nthEInp::content')]", N)
    else:
        enter_text_xpath(driver, "//input[@title='Limited']", limit)
    xpath_click_Xpath(driver, "//button[contains(@id,'1:bicoBtn')]")
    print("Completed Tab")


def Hiring(driver, M, R, C1, C2, C3, C4):
    # 3 Hiring Team Tab
    print("Job Requisition Hiring Tab Start")
    enter_text_clear_input_Xpath(driver, "//input[@aria-label='Hiring Manager']", M)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    try:
        xpath_click_Xpath(driver, "//span[text()='Yes']")
    except:
        pass
    enter_text_clear_input_Xpath(driver, "//input[@aria-label='Recruiter']", R)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    xpath_click_Xpath(driver, "//input[@_afov='0']")
    xpath_click_Xpath(driver, "//li[@_adfiv='1']")
    # Adding collaborates
    enter_text_xpath(driver, "//input[@aria-label='Collaborator']", C1)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    # add any other collaborates
    xpath_click_Xpath(driver, "//a[@title='Add Another Collaborator']")
    enter_num_text_Xapth(driver, '//input[@aria-label="Collaborator"]', C2, num=1)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    # add any other collaborates
    xpath_click_Xpath(driver, "//a[@title='Add Another Collaborator']")
    enter_num_text_Xapth(driver, '//input[@aria-label="Collaborator"]', C3, num=2)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    # add any other collaborates
    xpath_click_Xpath(driver, "//a[@title='Add Another Collaborator']")
    enter_num_text_Xapth(driver, '//input[@aria-label="Collaborator"]', C4, num=3)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    xpath_click_Xpath(driver, "//button[@title='Continue']")
    print("Completed Tab")


def Stucture(driver, T, L):
    # 4 Requisition Structure Tab
    print("Job Requisition Requisition Structure Tab Start")
    xpath_click_Xpath(driver, "//input[contains(@id,'rtSel::content')]")
    xpath_click_Xpath(driver, f"//ul[@aria-label='Recruiting Type']/li[@_adfiv='{T}']")
    xpath_click_Xpath(driver, "//input[@aria-label='Organization']")
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    enter_text_clear_input_Xpath(driver, "//input[@aria-label='Primary Location']", L)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    xpath_click_Xpath(driver, "//button[contains(@id,'bicoBtn')]")
    print("Completed Tab")


def Details(driver, L, T, S, J):
    # 5 Details Tab
    print("Job Requisition Details Tab Start")
    enter_text_xpath(driver, "//input[contains(@id,'mlSel::content')]", L)
    xpath_click_Xpath(driver, "//input[contains(@id,'ptSel::content')]")
    xpath_click_Xpath(driver, f"//ul[@aria-label='Full Time or Part Time']/li[@_adfiv='{T}']")
    xpath_click_Xpath(driver, "//input[contains(@id,'jsSel::content')]")
    xpath_click_Xpath(driver, f"//ul[@aria-label='Job Shift']/li[@_adfiv='{S}']")
    xpath_click_Xpath(driver, "//input[contains(@id,'jtSel::content')]")
    xpath_click_Xpath(driver, f"//ul[@aria-label='Job Type']/li[@_adfiv='{J}']")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb14')]")
    print("Completed Tab")


def Posting(driver):
    # 6 Position Description Tab
    print("Job Requisition Position Tab Start")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb15')]")
    print("Completed Tab")


def Offer(driver, W, WT, G, I):
    # 7 Offer info Tab
    print("Job Requisition Offer Tab Start")
    enter_text_clear_input_Xpath(driver, "//input[@aria-label='Primary Work Location']", W)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    enter_text_xpath(driver, "//input[contains(@id,'wtcSoc::content')]", WT)
    enter_text_clear_input_Xpath(driver, "//input[contains(@id,'grdIs::content')]", G)
    xpath_click_Xpath(driver, f"//tr[@aria-rowindex='{I}']")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb16')]")
    print("Completed Tab")


def Attach(driver, ):
    # 8 Attachment Tab
    print("Job Requisition Attachment Start")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb17')]")
    print("Completed Tab")


def Config(driver, A):
    # 9 Configurtion Tab
    print("Job Requisition Configurtion Start")
    xpath_click_Xpath(driver, "//*[contains(@id,'aorSel::content')]")
    xpath_click_Xpath(driver, f"//ul[@aria-label='Automatically Open Requisition for Sourcing']/li[@_adfiv='{A}']")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb18')]")
    print("Completed Tab")


def Question(driver, ):
    # 10 Question Tab
    print("Job Requisition Question Tab Start")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb19')]")


def Submit(driver):
    # Submit Button
    xpath_click_Xpath(driver, "//*[contains(@id,'UPsp1:SPsb2')]")
    xpath_click_Xpath(driver, "//*[contains(@id,'actwHm:PSEcil2')]")


# Requistion Interview
def Interview_SchedulesR(driver, R, J):
    xpath_click_Xpath(driver, f"//a[contains(@title,'{J}')]")
    xpath_click_Xpath(driver, "//*[contains(@id,'intrSdi::text')]")
    xpath_click_Xpath(driver, "//div[contains(@id,'isPce:PCEcil1')]")
    xpath_click_Xpath(driver, "//tr[contains(@id,'isPce:cischMi')]")
    xpath_click_Xpath(driver, "//input[contains(@id,'tmpSel::content')]")
    xpath_click_Xpath(driver, "//ul[@aria-label='Template']/li[@_adfiv='0']")
    xpath_click_Xpath(driver, "//td[contains(@id,'UPsp1:SPcf1')]")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb10')]")
    xpath_click_Xpath(driver, "//input[contains(@id,'typSel::content')]")
    xpath_click_Xpath(driver, "//ul[@aria-label='Format']/li[@_adfiv='2']")
    xpath_click_Xpath(driver, "//label[contains(@id,'sbc11Ck::Label0')]")
    enter_text_clear_input_Xpath(driver, "//input[contains(@id,'aIdSrh::content')]", R)
    xpath_click_Xpath(driver, "//tr[@aria-rowindex='1']")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb11')]")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb12')]")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb13')]")
    xpath_click_Xpath(driver, "//button[contains(@id,'GPcb14')]")
    xpath_click_Xpath(driver, "//div[contains(@id,'UPsp1:SPsb2')]")
    xpath_click_Xpath(driver, "//a[@title='Done']", sec=5)


# Fuction Add Candidates

# Data Function:
JobrequisitonItems = p.read_excel('Data.xlsx', 'Requistion')
# Login Recruiter
Url = "https://fa-ewwt-dev2-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/AtkHomePageWelcome?"
driver = setup_driver()
driver.get(Url)
xpath_click_Xpath(driver, "//*[@id='ssoBtn']")
xpath_click_Xpath(driver, "//*[@id='tilesHolder']/div[1]/div/div[1]")
print("Welcome Page")
# Home Pages
xpath_click_Xpath(driver, "//a[@title='Home']")
print("Home Page")
xpath_click_Xpath(driver,
                  "//div[@aria-controls='cluster_groupNode_workforce_management']//a[@name='groupNode_workforce_management']")
print("My Client Groups")
xpath_click_Xpath(driver, "//*[@id='itemNode_Recruiting_Hiring']")
print("Hiring Tab Open")

# Login Manager Change Manager Password and Username:
Url = "https://fa-ewwt-dev2-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/AtkHomePageWelcome?"
driver = setup_driver()
driver.get(Url)
enter_text_clear_input_Xpath(driver, "//*[@id='userid']", "GHogarth")
enter_text_clear_input_Xpath(driver, "//*[@id='password']", "%Dfjkn^3")
xpath_click_Xpath(driver, "//*[@id='btnActive']")
print("Welcome Page")
# Home Pages
xpath_click_Xpath(driver, "//a[@title='Home']")
print("Home Page")
xpath_click_Xpath(driver,
                  "//div[@aria-controls='cluster_groupNode_workforce_management']//a[@name='groupNode_workforce_management']")
print("My Client Groups")
xpath_click_Xpath(driver, "//*[@id='itemNode_Recruiting_Hiring']")
print("Hiring Tab Open")

# Multiple Requisition adding
for x in range(0, len(JobrequisitonItems['job_title'])):
    # Job Requistion Page
    xpath_click_Xpath(driver, "//div[@title='Job Requisitions']/a")
    print("Job Requisition Tab")
    xpath_click_Xpath(driver, "//div[@title='Create Job Requisition']/a")
    print("Job Requisition Add")

    # Add Requisition Page
    # 1 How Tab
    # Variable
    Type = JobrequisitonItems['recruiting_type'][x]
    Unit = JobrequisitonItems['business_unit'][x]
    Title = JobrequisitonItems['job_title'][x]
    Use = JobrequisitonItems['use'][x]
    Index = JobrequisitonItems['rowindex'][x]
    # Function
    driver
    How(driver, Type, Unit, Title, Use, Index)
    Job = JobrequisitonItems['job_use'][x]
    Limit = JobrequisitonItems['Limit'][x]
    N = JobrequisitonItems['Number'][x]
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Basic(driver, Job, Limit, N)
    M = JobrequisitonItems['hiring_manager'][x]
    R = JobrequisitonItems['recruiter'][x]
    C1 = JobrequisitonItems['collaborator0'][x]
    C2 = JobrequisitonItems['collaborator1'][x]
    C3 = JobrequisitonItems['collaborator2'][x]
    C4 = JobrequisitonItems['collaborator3'][x]
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Hiring(driver, M, R, C1, C2, C3, C4)
    L = JobrequisitonItems['primary_location'][x]
    T = JobrequisitonItems['RecruitingType'][x]

    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Stucture(driver, T, L)
    L = JobrequisitonItems['job_level'][x]
    T = JobrequisitonItems['Full_Time_Part_Time'][x]
    S = JobrequisitonItems['Shift'][x]
    J = JobrequisitonItems['JobType'][x]
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    # Function
    Details(driver, L, T, S, J)
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Posting(driver)
    # Function
    W = JobrequisitonItems['work_location'][x]
    WT = JobrequisitonItems['work_type'][x]
    G = JobrequisitonItems['Grade'][x]
    I = JobrequisitonItems['GradeIndex'][x]
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Offer(driver, W, WT, G, I)
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Attach(driver)
    A = JobrequisitonItems['AutomicallyPosted'][x]
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Config(driver, A)
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    Question(driver)
    # Function
    driver.execute_script("window.scrollTo(0, window.scrollY - 500)")
    Submit(driver)
    print(f"Done {JobrequisitonItems['job_title'][x]}-{x}")
    R = JobrequisitonItems['recruiter'][x]
    J = JobrequisitonItems['job_title'][x]
    Interview_SchedulesR(driver, R)