import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure
from datetime import datetime

# ------------------------
# Command-line option to select browser
# ------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome OR firefox"
    )

# ------------------------
# Fixture for browser setup
# ------------------------
@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = FFOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FFService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome or firefox.")

    request.cls.driver = driver
    yield
    driver.quit()

# ------------------------
# Screenshot helper
# ------------------------
# def take_screenshot(driver, name="screenshot"):
#     timestamp = datetime.now().strftime("%H-%M-%S_%m-%d-%Y")
#     screenshot_name = f"{name}_{timestamp}.png"
#
#     screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#     os.makedirs(screenshot_dir, exist_ok=True)
#     screenshot_path = os.path.join(screenshot_dir, screenshot_name)
#
#     driver.save_screenshot(screenshot_path)
#
#     # Attach to Allure
#     with open(screenshot_path, "rb") as f:
#         allure.attach(
#             f.read(),
#             name=screenshot_name,
#             attachment_type=allure.attachment_type.PNG
#         )
#
#     print(f"📸 Screenshot saved: {screenshot_path}")
#     return screenshot_path
#
# # ------------------------
# # Pytest hook: capture screenshot on failure
# # ------------------------
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Capture screenshot on test failure automatically
#     """
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         driver = getattr(item.instance, "driver", None)
#         if driver:
#             take_screenshot(driver, name=item.name)
