import pytest
from playwright.sync_api import Browser,Page

@pytest.fixture()
def startsaucedemo(browser:Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    yield page 
