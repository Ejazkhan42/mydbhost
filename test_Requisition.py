import time

import pytest

from  Helper.packages.requirments import (setup_driver as driver,
                                          xpath_click_Xpath as XapthClick,
                                          dropdownEnter as dropText,
                                          dropdownXapth as dropXath,
                                          enter_text_xpath as XapthText,
                                          enter_text_clear_input_Xpath as ClearTexTXapth, Base_Url,Requisition,RType,
                                          )
from Helper.objects.LoginObjects import login,Home,Job_Requisition as Rq,continue_buttons as btn


@pytest.fixture
def Login_without_SSO(test_driver):
    Login = Base_Url()
    Requisition_Data = Requisition()
    driver = test_driver
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
    for x in range(0, len(Requisition_Data)):
        ReqType = Requisition_Data["ReqType"][x]
        Use = Requisition_Data["Use"][x]
        BusinessUnit = Requisition_Data["BusinessUnit"][x]
        Position = Requisition_Data["Position"][x]
        RecruitingType = Requisition_Data["RecruitingType"][x]
        PrimaryLocation = Requisition_Data["PrimaryLocation"][x]
        RequisitionTemplate = Requisition_Data["RequisitionTemplate"][x]
        Job = Requisition_Data["Job"][x]
        limited = Requisition_Data["limited"][x]
        NumberoffJob = Requisition_Data["NumberoffJob"][x]
        RequistionsName = Requisition_Data["RequistionsName"][x]
        Hiring_ManagerName = Requisition_Data["Hiring_ManagerName"][x]
        RecruiterName = Requisition_Data["RecruiterName"][x]
        CollaboratorName1 = Requisition_Data["CollaboratorName1"][x]
        CollaboratorName2 = Requisition_Data["CollaboratorName2"][x]
        CollaboratorName3 = Requisition_Data["CollaboratorName3"][x]
        CollaboratorName4 = Requisition_Data["CollaboratorName4"][x]
        RequisitionType = Requisition_Data["RequisitionType"][x]
        RequisitionOragnzation = Requisition_Data["RequisitionOragnzation"][x]
        ReqPrimaryLocation = Requisition_Data["ReqPrimaryLocation"][x]
        workerType = Requisition_Data["workerType"][x]
        ReqularTemp = Requisition_Data["ReqularTemp"][x]
        FullOrPartTypes = Requisition_Data["FullOrPartTypes"][x]
        Travel = Requisition_Data["Travel"][x]
        LegalEmployer = Requisition_Data["LegalEmployer"][x]
        workplace = Requisition_Data["workplace"][x]
        CSP = Requisition_Data["CSP"][x]
        Requisition_Add(driver, ReqType, Use, BusinessUnit,
                        Position, RecruitingType,
                        PrimaryLocation, RequisitionTemplate, Job, limited,
                        NumberoffJob, RequistionsName,
                        Hiring_ManagerName, RecruiterName, CollaboratorName1, CollaboratorName2, CollaboratorName3,
                        CollaboratorName4,
                        RequisitionType, RequisitionOragnzation, ReqPrimaryLocation,
                        workerType, ReqularTemp, FullOrPartTypes,
                        Travel, LegalEmployer,
                        workplace, CSP)
    driver.quit()


def Welcome(driver):
    XapthClick(driver, Home.Home_Button())
    XapthClick(driver, Home.MyClient_Group())
    XapthClick(driver, Home.Hiring_Tab())


def Requisition_Add(driver, ReqType, Use, BusinessUnit,
                    Position, RecruitingType,
                    PrimaryLocation, RequisitionTemplate, Job, limited,
                    NumberoffJob, RequistionsName,
                    Hiring_ManagerName, RecruiterName, CollaboratorName1, CollaboratorName2, CollaboratorName3,
                    CollaboratorName4,
                    RequisitionType, RequisitionOragnzation, ReqPrimaryLocation,
                    workerType, ReqularTemp, FullOrPartTypes,
                    Travel, LegalEmployer,
                    workplace, CSP):
    XapthClick(driver, Rq.tab())
    XapthClick(driver, Rq.add())
    used = How(driver, ReqType, Use, BusinessUnit, Position, RecruitingType, PrimaryLocation, RequisitionTemplate, Job,
               RequistionsName)
    Basic(driver, used, limited, NumberoffJob, RequistionsName)
    HiringTeam(driver, Hiring_ManagerName, RecruiterName, CollaboratorName1, CollaboratorName2, CollaboratorName3,
               CollaboratorName4)
    RequisitionStructure(driver, RequisitionType, RequisitionOragnzation, ReqPrimaryLocation)
    Details(driver, workerType, ReqularTemp, FullOrPartTypes)
    WorkRequirements(driver, Travel)
    PostingDescription(driver)
    skills(driver)
    offerInfo(driver, LegalEmployer, workplace)
    EstimatedTimetoHire(driver)
    Attachments(driver)
    Configuration(driver, CSP)
    Questionnaires(driver)


def How(driver, ReqType, Use, BusinessUnit, Position, RecruitingType, PrimaryLocation, RequisitionTemplate, Job,
        RequistionsName):
    XapthClick(driver, Rq.ReqType())
    Type = RType(ReqType)
    XapthClick(driver, Rq.Type_pipline1_or_standard0(Type))
    XapthClick(driver, Rq.uses())
    used = RType(Use)
    if used == 0:
        XapthClick(driver, Rq.use_Type(used))
        XapthClick(driver, Rq.recruitng_Type_H())
        Type = RType(RecruitingType)
        XapthClick(driver, Rq.recruiting_drop_down_select(Type))
        XapthText(driver, Rq.primary_location(), PrimaryLocation)
        XapthClick(driver, Rq.rowIndex(1))
        XapthText(driver, Rq.template(), RequisitionTemplate)
        XapthClick(driver, btn.BI0())
    elif used == 1:
        XapthClick(driver, Rq.use_Type(used))
        XapthText(driver, Rq.business_unit(), BusinessUnit)
        XapthClick(driver, Rq.business1(),post=1)
        XapthText(driver, Rq.position(), Position)
        XapthClick(driver, Rq.position1(),post=1)
        XapthClick(driver, btn.BI0())
    elif used == 2:
        XapthClick(driver, Rq.use_Type(used))
        XapthText(driver, Rq.business_unit(), BusinessUnit)
        XapthClick(driver, Rq.business1(),post=1)
        XapthText(driver, Rq.job(), Job)
        XapthClick(driver, Rq.job1(),post=1)
        XapthClick(driver, btn.BI0())
    elif used == 3:
        XapthClick(driver, Rq.use_Type(used))
        XapthText(driver, Rq.requisition_Ex(), RequistionsName)
        XapthClick(driver, Rq.rowIndex(1))
        XapthClick(driver, btn.BI0())
    elif used == 4:
        XapthClick(driver, Rq.use_Type(used))
        XapthClick(driver, btn.BI0())
    return used


def Basic(driver, used, limited, NumberoffJob, RequistionsName):
    if used == 1 or used == 2 or used == 3:
        XapthText(driver, Rq.limited(), limited)
        if limited == 'Limited':
            ClearTexTXapth(driver, Rq.number_off_jobs(), str(NumberoffJob))
            XapthClick(driver, btn.BI1())
    elif used == 4:
        XapthText(driver, Rq.requisition_Name(), RequistionsName)
        XapthText(driver, Rq.limited(), limited)
        if limited == 'Limited':
            ClearTexTXapth(driver, Rq.number_off_jobs(), NumberoffJob)
            XapthClick(driver, btn.BI1())
    else:
        XapthClick(driver, btn.BI1())


def HiringTeam(driver, Hiring_ManagerName, RecruiterName, CollaboratorName1, CollaboratorName2, CollaboratorName3,
               CollaboratorName4):
    ClearTexTXapth(driver, Rq.hiring_M(), Hiring_ManagerName)
    XapthClick(driver, Rq.rowIndex(1))
    try:
        XapthClick(driver, Rq.yes())
    except:
        pass
    ClearTexTXapth(driver, Rq.recruiter(), RecruiterName)
    XapthClick(driver, Rq.rowIndex(1))
    if not str(CollaboratorName1) == 'nan':
        XapthClick(driver, Rq.collaborator_T())
        XapthClick(driver, Rq.collabortor_or_work_council())
        XapthText(driver, Rq.add_colloborator(), CollaboratorName1)
        XapthClick(driver, Rq.rowIndex(1))

    if not str(CollaboratorName2) == 'nan':
        XapthClick(driver, Rq.add_other_colloborator())
        XapthText(driver, Rq.add_other_colloborator, CollaboratorName2)
        XapthClick(driver, Rq.rowIndex(1))
    if not str(CollaboratorName3) == 'nan':
        XapthClick(driver, Rq.add_other_colloborator())
        XapthText(driver, Rq.add_other_colloborator, CollaboratorName3)
        XapthClick(driver, Rq.rowIndex(1))
    if not str(CollaboratorName4) == 'nan':
        XapthClick(driver, Rq.add_other_colloborator())
        XapthText(driver, Rq.add_other_colloborator, CollaboratorName4)
        XapthClick(driver, Rq.rowIndex(1))
    XapthClick(driver, btn.GP12())


def RequisitionStructure(driver, RequisitionType, RequisitionOragnzation, ReqPrimaryLocation):
    XapthClick(driver, Rq.recruitng_Type())
    Type = RType(RequisitionType)
    XapthClick(driver, Rq.recruiting_drop_down_select(Type))
    time.sleep(2)
    XapthText(driver, Rq.oragnzation(), RequisitionOragnzation)
    XapthClick(driver, Rq.rowIndex(1))
    time.sleep(2)
    XapthText(driver, Rq.primary_location(), ReqPrimaryLocation)
    XapthClick(driver, Rq.rowIndex(1))
    time.sleep(2)
    XapthClick(driver, btn.BI1())


def Details(driver, workerType, ReqularTemp, FullOrPartTypes):
    XapthClick(driver, Rq.workerTypes())
    Type = RType(workerType)
    XapthClick(driver, Rq.workerType(Type))
    XapthClick(driver, Rq.FTimePTime())
    Type = RType(FullOrPartTypes)
    XapthClick(driver, Rq.FTimeorPTime(Type))
    XapthClick(driver, Rq.recruitng_Type())
    Type = RType(ReqularTemp)
    XapthClick(driver, Rq.RegularTemp(Type))
    XapthClick(driver, btn.GP14())


def WorkRequirements(driver, Travel):
    XapthClick(driver, Rq.Travel())
    Type = RType(Travel)
    XapthClick(driver, Rq.TravelYN(Type))
    XapthClick(driver, btn.GP15())


def PostingDescription(driver):
    XapthClick(driver, btn.GP16())


def skills(driver):
    XapthClick(driver, btn.GP17())


def offerInfo(driver, LegalEmployer, workplace):
    ClearTexTXapth(driver, Rq.legalEmp(), LegalEmployer)
    XapthClick(driver, Rq.rowIndex(1))
    XapthClick(driver, Rq.workplace())
    Type = RType(workplace)
    XapthClick(driver, Rq.Wplaces(Type))
    XapthClick(driver, btn.GP18())


def EstimatedTimetoHire(driver):
    XapthClick(driver, btn.GP19())


def Attachments(driver):
    XapthClick(driver, btn.GP110())


def Configuration(driver, CSP):
    XapthClick(driver, Rq.CandidatesSelectionP())
    XapthClick(driver, Rq.selectionP(CSP))
    XapthClick(driver, btn.GP111())


def Questionnaires():
    XapthClick(driver, btn.Submit())

@pytest.mark.login
def test_login_without_sso(Login_without_SSO):
    pass