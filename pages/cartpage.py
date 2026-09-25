from playwright.sync_api import Page
from playwright.sync_api import Browser

class Cart:
     
     def __init__(self,page:Page):
          self._carttilevalidation = page.get_by_text("Your Cart", exact=True)
          self._checkoutctaclick = page.locator("#checkout")

     def checkoutclick(self):
          self._checkoutctaclick.click()

     def cartpagevalidation(self):
           assert self._carttilevalidation.inner_text() == "Your Cart"

     def checkout(self):
          self.cartpagevalidation()
          self.checkoutclick()
      

          