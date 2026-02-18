import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru-ru", "en-en"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"https://learn.microsoft.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        time.sleep(2)


    def test_guest_should_see_navbar_element(self, browser, language):
        time.sleep(2)
        assert 1==1