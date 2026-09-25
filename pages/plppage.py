from playwright.sync_api import Page
from playwright.sync_api import Browser

class PLP:
    def __init__(self,page:Page):
        self._pagetitle = page.locator('[data-test="title"]').filter(has_text="Products")
        self._addtocart = page.get_by_role("button", name="Add to cart").nth(0)
        self._removecart = page.get_by_role("button", name="Remove").nth(0)
        self._minicarticon = page.locator(".shopping_cart_badge")

    def plptitlevalidation(self):
        assert self._pagetitle.inner_text() == "Products"

    def productadd(self):
        self._addtocart.click()

    def productremove(self):
        self._removecart.click()       
    
    def productaddedvalidation(self):
        assert self._removecart.inner_text() == "Remove"

    def productremovedvalidation(self):
        assert self._addtocart.inner_text() == "Add to cart"

    def minicarticonclick(self):
        self._minicarticon.click()            

    def addtocart(self):
        self.plptitlevalidation()
        self.productadd()
        self.productaddedvalidation()

    def removetocart(self):
        self.productremove()
        self.productremovedvalidation()
        



