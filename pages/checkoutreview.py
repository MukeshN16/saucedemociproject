from playwright.sync_api import Page
from playwright.sync_api import Browser

class Checkoutreview:

    def __init__(self,page:Page):
        self._quantitycheck = page.locator(".cart_quantity_label")
        self._descriptioncheck = page.locator(".cart_desc_label")
        self._paymentinformationcheck = page.get_by_text("Payment Information:",exact=True)
        self._shippinginformationcheck = page.get_by_text("Shipping Information:",exact=True)
        self._totalpricecheck = page.get_by_text("Price Total",exact=True)
        self._finaltotalcheck = page.locator(".summary_total_label")
        self._finishCTAcheck = page.locator("#finish")

    def quantityavailable(self):
        assert self._quantitycheck.inner_text() == "QTY"

    def descriptioncheck(self):
        assert self._descriptioncheck.inner_text() == "Description"

    def paymentinformationcheck(self):
        assert self._paymentinformationcheck.inner_text() == "Payment Information:"    

    def shippinginformationcheck(self):
        assert self._shippinginformationcheck.inner_text() == "Shipping Information:"

    def totalpricecheck(self):
        assert self._totalpricecheck.inner_text() == "Price Total" 

    def finaltotalcheck(self):
        assert self._finaltotalcheck.inner_text().startswith("Total:")

    def finishcta(self):
        self._finishCTAcheck.click()    

    def checkoutreview(self):
        self.quantityavailable()
        self.descriptioncheck()
        self.paymentinformationcheck()
        self.shippinginformationcheck()
        self.totalpricecheck()
        self.finaltotalcheck()
        self.finishcta()




