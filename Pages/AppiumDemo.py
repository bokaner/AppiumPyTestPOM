from Pages.BasePage import BasePage
from Pages.BasePageTwo import BasePageTwo


class AppiumDemo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def clickonEnterSomevalueButton(self):
        self.click("entersomevalueBtn_ID")
        #self.clickElement("entersomevalueBtn_ID")

    def entersomeValue(self, text):
        self.type("entervaluetext_ID", text)

    def verify_the_title(self):
        return self.getText("entertitle_XPATH")

    def verify_entersome_button_isDisplayed(self):
        return self.isDisplayed("entersomevalueBtn_ID")

