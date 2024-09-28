import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from dotenv import load_dotenv
import os
from appium import webdriver
from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Python project wiki",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test wikipedia",

            "userName": os.getenv('USER_NAME'),
            "accessKey": os.getenv('ACCESS_KEY')
        }
    })
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub",
                                             options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    session_id = browser.driver.session_id
    attach.add_video(session_id)

    browser.quit()


