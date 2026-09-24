from playwright.sync_api import Browser
from playwright.sync_api import Page
from pages.loginpage import Login

def test_login_standarduser(startsaucedemo):
    login = Login(startsaucedemo)
    login.standarduserlogin()

def test_login_visualuser(startsaucedemo):
    login = Login(startsaucedemo)
    login.visualuserlogin()

   