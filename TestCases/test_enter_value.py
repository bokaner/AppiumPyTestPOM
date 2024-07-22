import time

import pytest

from Pages.AppiumDemo import AppiumDemo
from TestCases.BaseTest import BaseTest
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

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_validate_Text(self):
        self.ap = AppiumDemo(self.driver)
        displayed= self.ap.verify_entersome_button_isDisplayed()
        print(displayed)
        self.ap.clickonEnterSomevalueButton()
        title = self.ap.verify_the_title()
        assert title == "Enter some "
        print(title)
        self.ap.entersomeValue("ujjwal")


