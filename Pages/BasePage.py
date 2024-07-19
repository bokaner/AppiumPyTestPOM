import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = None
        try:
            if str(locator).endswith("_XPATH"):
                element = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator))
                element.click()
            elif str(locator).endswith("_ACCESSIBILITYID"):
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                                   configReader.readConfig("locators", locator))
                element.click()
            elif str(locator).endswith("_ID"):
                element = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator))
                element.click()
            log.logger.info("Clicking on an element: " + str(locator))
        except Exception as e:
            # Handle the exception (e.g., log the error, raise an alert, etc.)
            log.logger.error(f"An error occurred while clicking on {locator}: {e}")
            raise  # Re-raise the exception if you want to propagate it further
        return element

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(AppiumBy.XPATH, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator))[
                index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(AppiumBy.ID, configReader.readConfig("locators", locator))[index].click()
        #log.logger.info("Clicking on an Element "+ str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(value))


    def isDisplayed(self, locator):
        #element = None
        try:
            if str(locator).endswith("_XPATH"):
                element = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator))
                element.is_displayed()
                log.logger.info("Clicking on an element: " + str(locator))
                return True
            elif str(locator).endswith("_ACCESSIBILITYID"):
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                                   configReader.readConfig("locators", locator))
                element.is_displayed()
                log.logger.info("Clicking on an element: " + str(locator))
                return True
            elif str(locator).endswith("_ID"):
                element = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator))
                element.is_displayed()
                log.logger.info("Clicking on an element: " + str(locator))
                return True
        except Exception as e:
            # Handle the exception (e.g., log the error, raise an alert, etc.)
            log.logger.error(f"An error occurred while clicking on {locator}: {e}")
            raise  # Re-raise the exception if you want to propagate it further
        return False

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH,configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element " + str(locator))

        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element "+ str(locator))

        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID,configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element "+ str(locator))
        return text
