from playwright.sync_api import Page
from playwright.sync_api import Browser

class Login:

    def __init__(self,page:Page):
        self._enterusername = page.get_by_placeholder("Username")
        self._enterpasword = page.get_by_placeholder("Password")
        self._clickloginbutton = page.locator("#login-button")

    def enterusername(self):
        self._enterusername.fill("standard_user")

    def entervisualusername(self):
        self._enterusername.fill("visual_user")    

    def enterpassword(self):
        self._enterpasword.fill("secret_sauce")

    def clickloginbutton(self):
        self._clickloginbutton.click()

    def standarduserlogin(self):
        self.enterusername()
        self.enterpassword()
        self.clickloginbutton()

    def visualuserlogin(self):
        self.entervisualusername()
        self.enterpassword()
        self.clickloginbutton()


        
        