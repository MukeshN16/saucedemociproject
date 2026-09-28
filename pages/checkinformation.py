from playwright.sync_api import Page
from playwright.sync_api import Browser

class Checkoutinformation:
 
 def __init__(self,page:Page):
  self._enterfirstname = page.get_by_placeholder("First Name")
  self._enterlastname = page.get_by_placeholder("Last Name")
  self._enterzipcode = page.get_by_placeholder("Zip/Postal Code")
  self._continuebutton = page.locator("#continue")


 def eneterfirstname(self):
    self._enterfirstname.fill("test")

 def enterlastname(self):   
   self._enterlastname.fill("testlast")

 def enterzipcode(self):
   self._enterzipcode.fill("111111")

 def clickcontinue(self):
  self._continuebutton.click()

 def entercheckoutinformation(self):
   self.eneterfirstname()
   self.enterlastname()
   self.enterzipcode()
   self.clickcontinue()  
       
  
 