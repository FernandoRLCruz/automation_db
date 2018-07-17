import unittest
from selenium import webdriver
import pages
from locators import *
from selenium.webdriver.common.by import By


class TestPages(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = pages.webdriver.Firefox()
        self.driver.get("http://demo.cs-cart.com/")

    '''def test_page_load(self):
        page = pages.MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())'''

    def test_search_item(self):
        page = pages.MainPage(self.driver)
        page.search_item("Batman")
        page.click_image()
        page.click_carrinho()


    '''def test_sign_up_button(self):
        print "\n" + str(test_cases(2))
        page = MainPage(self.driver)
        signUpPage = page.click_sign_up_button()
        self.assertIn("ap/register", signUpPage.get_url())

    def test_sign_in_button(self):
        print "\n" + str(test_cases(3))
        page = MainPage(self.driver)
        loginPage = page.click_sign_in_button()
        self.assertIn("ap/signin", loginPage.get_url())

    def test_sign_in_with_valid_user(self):
        print "\n" + str(test_cases(4))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user("valid_user")
        self.assertIn("yourstore/home", result.get_url())

    def test_sign_in_with_in_valid_user(self):
        print "\n" + str(test_cases(5))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("invalid_user")
        self.assertIn("There was a problem with your request", result)'''

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main ()
