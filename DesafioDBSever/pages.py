from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage (Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).click()
        self.find_element(*self.locator.SEARCH).clear()
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)

    def click_image(self):
        self.hover(*self.locator.IMAGE_BATMAN)
        self.find_element(*self.locator.IMAGE_BATMAN).click()

    def click_carrinho(self):
        self.hover(*self.locator.BUTTON_CARRINHO)
        self.find_element(*self.locator.BUTTON_CARRINHO).click()