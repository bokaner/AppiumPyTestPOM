import time

import pytest

from Pages.AppiumDemo import AppiumDemo
from TestCases.BaseTest import BaseTest
from TestCases.conftest import allureLogs
from Utilities import dataProvider
import allure


class Test_Entervalue(BaseTest):

    @pytest.mark.parametrize("items", dataProvider.get_data("appdataTest"))
    def test_validate_Text(self, items):
        self.ap = AppiumDemo(self.driver)
        self.ap.clickonEnterSomevalueButton()
        self.ap.verify_the_title()
        self.ap.entersomeValue(items)

    #  def test_verify_Text(self, items):
    #   appiumdemo = AppiumDemo(self.driver)
    #    appiumdemo.clickonEnterSomevalueButton()
    #      appiumdemo.entersomeValue(items)

    @allure.description("this test case is to validate the text writtent on the Page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_validate_Text(self):
        self.ap = AppiumDemo(self.driver)
        allureLogs("Checking the button is displayed ")

        displayed= self.ap.verify_entersome_button_isDisplayed()
        #allureLogs("")
        print(displayed)
        #allureLogs()
        self.ap.clickonEnterSomevalueButton()
        allureLogs("button clicked successfully")

        title = self.ap.verify_the_title()
        assert title == "Enter some Value"
        print(title)
        self.ap.entersomeValue("ujjwal")


