class login:
    def loginButton():
        return "//*[@id='btnActive']"
    def username_xapth():
        return "//*[@id='userid']"
    def password_xapth():
        return "//*[@id='password']"
class SSO_Login:
    def SSO_Button():
        return "//*[@id='ssoBtn']"
    def Mic_Login_button():
        return "//*[@id='tilesHolder']/div[1]/div/div[1]"
class Home:
    def Home_Button():
        return "//a[@title='Home']"
    def MyClient_Group():
        return "//div[@aria-controls='cluster_groupNode_workforce_management']//a[@name='groupNode_workforce_management']"
    def Hiring_Tab():
        return "//*[@id='itemNode_Recruiting_Hiring']"
class continue_buttons:
    def Save():
        return "//div[contains(@id,'UPsp1:APscl2')]"
    def Done():
        return  "//a[@title='Done']"
    def Submit():
        return "//div[contains(@id,'UPsp1:SPsb2')]"
    def BI0():
        return "//button[contains(@id,'0:bicoBtn')]"
    def BI1():
        return "//button[contains(@id,'1:bicoBtn')]"
    def BI2():
        return "//button[contains(@id,'2:bicoBtn')]"
    def BI3():
        return "//button[contains(@id,'3:bicoBtn')]"
    def BI4():
        return "//button[contains(@id,'4:bicoBtn')]"
    def BI5():
        return "//button[contains(@id,'5:bicoBtn')]"
    def GP10():
        return "//button[contains(@id,'GPcb10')]"
    def GP11():
        return "//button[contains(@id,'GPcb11')]"
    def GP12():
        return "//button[contains(@id,'GPcb12')]"
    def GP13():
        return "//button[contains(@id,'GPcb13')]"
    def GP14():
        return "//button[contains(@id,'GPcb14')]"
    def GP15():
        return "//button[contains(@id,'GPcb15')]"
    def GP16():
        return "//button[contains(@id,'GPcb16')]"
    def GP17():
        return "//button[contains(@id,'GPcb17')]"
    def GP18():
        return "//button[contains(@id,'GPcb18')]"
    def GP28():
        return "//button[contains(@id,'GPcb28')]"
    def GP19():
        return "//button[contains(@id,'GPcb19')]"
    def GP110():
        return "//button[contains(@id,'GPcb110')]"
    def GP111():
        return "//button[contains(@id,'GPcb111')]"




class Job_Requisition:
    def tab():
        return "//div[@title='Job Requisitions']/a"
    def add():
        return "//div[@title='Create Job Requisition']/a"  
    #How Tab
    def requisition_Name():
        return "//input[contains(@id,'tieInp::content')]"
    def ReqType():
        return "//input[contains(@id,'reTySel::content')]"
    def Type_pipline1_or_standard0(Type):
        return f"//ul[@aria-label='Requisition Type']/li[@_adfiv='{Type}']"
    def uses():
        return "//input[contains(@id,'sourSel::content')]"
    def use_Type(Type):
        return f"//ul[@aria-label='Use']/li[@_adfiv='{Type}']"
    def business_unit():
        return "//input[contains(@id,'buIs::content')]"
    def rowIndex(I=1):
        return f"//tr[@aria-rowindex='{I}']"
    def position():
        return "//input[contains(@id,'posIs::content')]"
    def job():
        return "//input[contains(@id,'jobIs::content')]"
    def exiting_Title():
        return "//input[contains(@id,'reqIs::content')]"
    def business1():
        return "//*[contains(@id,'buIs::item0')]"
    def job1():
        return "//*[contains(@id,'jobIs::item0')]"
    def position1():
        return "//*[contains(@id,'posIs::item0')]"
    #Basic Tab
    def limited():
        return "//input[contains(@id,'nofoSel::content')]"
    def number_off_jobs():
        return "//input[contains(@id,'nthEInp::content')]"
    #Hiring Tab
    def hiring_M():
        return "//input[@aria-label='Hiring Manager']"
    def yes(Y='Yes'):
        return f"//span[text()='{Y}']"
    def recruiter():
        return "//input[@aria-label='Recruiter']"
    def collaborator_T():
        return "//input[contains(@id,'cTypSel::content')]"
    def collabortor_or_work_council(C=1):
        return f"//li[@_adfiv='{C}']"
    def add_colloborator():
        return "//input[@aria-label='Collaborator']"
    def add_other_colloborator():
        return "//a[@title='Add Another Collaborator']"
    def add_work_council():
        return "//input[@aria-label='Works councils Representative']"
    #Structure Tab
    def recruitng_Type():
        return "//input[contains(@id,'rtSel::content')]"
    def recruiting_drop_down_select(T):
        return f"//ul[@aria-label='Recruiting Type']/li[@_adfiv='{T}']"
    def oragnzation():
        return "//input[contains(@id,'orgSis:orgIs::content')]"
    def primary_location():
        return "//input[@aria-label='Primary Location']"  
    #Details Tab
    def workerTypes():
        return "//input[contains(@id,'wtSel::content')]"
    def workerType(T):
        return f"//ul[@aria-label='Worker Type']/li[@_adfiv='{T}']"
    def FTimePTime():
        return "//input[contains(@id,'ptSel::content')]"
    def FTimeorPTime(T):
        return f"//ul[@aria-label='Full Time or Part Time']/li[@_adfiv='{T}']"
    def RegularTemp(T):
        return f"//ul[@aria-label='Regular or Temporary']/li[@_adfiv='{T}']"
    def Education():
        return "//input[contains(@id,':slSel::content')]"
    def EducationLevel(T):
        return f"//ul[@aria-label='Education Level']/li[@_adfiv='{T}']"
    #WorkRequirements
    def Travel():
        return "//input[contains(@id,'ntrSel::content')]"
    def TravelYN(T):
        return f"//ul[@aria-label='Travel Required']/li[@_adfiv='{T}']"
    #Work Requirements
    #Offer Info Tab
    def legalEmp():
        return "//input[contains(@id,'leSis:leIs::content')]"
    def workplace():
        return "//input[contains(@id,'wtcSoc::content')]"
    def Wplaces(T):
        return f"//ul[contains(@id,'wtcSoc::pop')]/li[@_adfiv='{T}']"
    def recruitng_Type_H():
        return "//input[contains(@id,'0:retpSel::content')]"
    def template():
        return "//input[contains(@id,'tmpSis:tmpIs::content')]"
    def requisition_Ex():
        return "//input[contains(@id,'reqSis:reqIs::content')]"
    #Configuration
    def CandidatesSelectionP():
        return "//input[contains(@id,'cspSel::content')]"
    def selectionP(T):
        return f"//ul[@aria-label='Candidate Selection Process']/li[@_adfiv='{T}']"



class Candidates:
    def Candidates_Tab():
        return "//div[@title='Candidate Search']/a"
    def Search_Candidates_Button():
        return "//div[contains(@id,'cb4Btn')]"
    def add_button():
        return "//div[contains(@id,'addBtn')]"
    def FirstName_Input():
        return "//input[contains(@id,'fnEInp::content')]"
    def LastName_Input():
        return "//input[contains(@id,'lnEInp::content')]"
    def Email_Input():
        return "//input[contains(@id,'it3Inp::content')]"
    def Save_and_close_button():
        return "//div[contains(@id,'UPsp1:APscl2')]"
    def Yes_button():
        return "//div[contains(@id,'hm1:PSEcil2')]"
    def Done_Button():
        return  "//a[@title='Done']"
    def CandidatesNumber():
        return "//td[contains(@id,'SPph::_afrTtxt')]"
        
        