import pytest


@pytest.mark.flaky(reruns=1)
@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest:
    pass
