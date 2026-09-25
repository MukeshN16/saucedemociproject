from playwright.sync_api import Browser
from playwright.sync_api import Page
from pages.loginpage import Login
from pages.plppage import PLP
from pages.cartpage import Cart

def test_checkout(startsaucedemo):
    login = Login(startsaucedemo)
    login.standarduserlogin()
    plp = PLP(startsaucedemo)
    plp.addtocart()
    plp.minicarticonclick()
    cart = Cart(startsaucedemo)
    cart.checkout()

    


