from playwright.sync_api import Page
from playwright.sync_api import Browser

class Ordersuccess:

    def __init__(self,page:Page):
     self._thankyouvalidation = page.get_by_text("Thank you for your order!",exact=True)
     self._orderdispatchvalidation = page.get_by_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!",exact=True)
     self._backtohomecta = page.locator("#back-to-products")

    def thankyouvalidation(self):
       assert self._thankyouvalidation.inner_text() == "Thank you for your order!"

    def orderdispatchvalidation(self):
       assert self._orderdispatchvalidation.inner_text() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    def backtohomecta(self):
       self._backtohomecta.click()

    def ordersuccess(self):
       self.thankyouvalidation()
       self.orderdispatchvalidation()
       self.backtohomecta()     