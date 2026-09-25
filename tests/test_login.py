from playwright.sync_api import Browser
from playwright.sync_api import Page
from pages.loginpage import Login
from pages.plppage import PLP

def test_login_standarduser(startsaucedemo):
    login = Login(startsaucedemo)
    login.standarduserlogin()
    plp = PLP(startsaucedemo)
    plp.plptitlevalidation()

def test_login_visualuser(startsaucedemo):
    login = Login(startsaucedemo)
    login.visualuserlogin()
    plp = PLP(startsaucedemo)
    plp.plptitlevalidation()

   