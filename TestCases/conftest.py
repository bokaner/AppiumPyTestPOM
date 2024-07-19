import time
import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Hook to get the result of a test and attach it to the item."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    """Fixture to set up and tear down the Appium driver."""

    desired_caps = dict(
        platformName='Android',
        automationName='UiAutomator2',
        deviceName='emulator-5554',
        app='/Users/UJJIS/AppData/Local/Android/Sdk/platform-tools/Android_demo_App.apk',
        # appPackage = 'com.android.settings',
        # appActivity = '.Settings'
        appPackage='com.code2lead.kwad',
        appActivity='com.code2lead.kwad.MainActivity',
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(2)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    """Fixture to take a screenshot on test failure."""
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

