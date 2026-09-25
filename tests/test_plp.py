from playwright.sync_api import Browser
from playwright.sync_api import Page
from pages.loginpage import Login
from pages.plppage import PLP

def test_plpaddtocart(startsaucedemo):
    login = Login(startsaucedemo)
    login.standarduserlogin()
    plp = PLP(startsaucedemo)
    plp.addtocart() 
    plp.removetocart()
    plp.addtocart()
    plp.minicarticonclick()
