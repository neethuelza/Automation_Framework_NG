import allure  # For attaching screenshots and reporting
import pytest  # Pytest framework
from selenium.webdriver.support.wait import WebDriverWait  # For explicit waits
from selenium.webdriver.common.by import By  # For locating elements
from selenium.webdriver.support import expected_conditions as ec  # Expected conditions for waits
from datetime import datetime  # For timestamps

# Import your page objects
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils  # Utility functions, e.g., whoami(), URL, USERNAME, PASSWORD

@pytest.mark.usefixtures("test_setup")  # Apply test_setup fixture for driver initialization
class TestLogin:

    def test_login(self):
        """Test for logging in and verifying the dashboard title"""
        try:
            driver = self.driver  # Get driver from fixture
            driver.get(utils.URL)  # Open the application URL

            login = LoginPage(driver)  # Initialize login page object
            login.enter_username(utils.USERNAME)  # Enter username
            login.enter_password(utils.PASSWORD)  # Enter password
            login.click_login()  # Click login button

            # Wait until the dashboard heading is visible
            WebDriverWait(driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']"))
            )

            x = driver.title  # Get the current page title
            assert x == "ABC"  # Verify the title is as expected

        except AssertionError as error:
            # Handle assertion failures (e.g., title mismatch)
            print("Assertion error occurred")
            print(error)

            # Create a Windows-safe timestamp
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            test_name = utils.whoami()  # Get the current test name
            screenshot_name = test_name + "_" + current_time  # Combine test name and timestamp

            # Attach screenshot to Allure report
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )

            # Save screenshot physically in the screenshots folder
            self.driver.get_screenshot_as_file(
                "C:/Users/abyja/PycharmProjects/Automation_Framework_NG/screenshots/" + screenshot_name + ".png"
            )

            # Save physical screenshot
            # import os
            # os.makedirs("C:/Users/abyja/PycharmProjects/Automation_Framework_NG/screenshots", exist_ok=True)
            # screenshot_path = "C:/Users/abyja/PycharmProjects/Automation_Framework_NG/screenshots/" + screenshot_name + ".png"
            # self.driver.get_screenshot_as_file(screenshot_path)

            raise  # Re-raise to mark test as failed

        except Exception as e:
            # Handle any unexpected exceptions
            print("An unexpected exception occurred:", e)

            # Create Windows-safe timestamp
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            test_name = utils.whoami()
            screenshot_name = test_name + "_" + current_time

            # Attach screenshot to Allure report
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )

            # Note: Physical screenshot save is not included here, can add same as above if needed
            raise  # Re-raise to mark test as failed

        else:
            # Executed if no exceptions occur
            print("No exceptions occurred")

        finally:
            # Executed regardless of test outcome
            print("This block will always execute | Close DB")

    def test_logout(self):
        """Test for logging out from the application"""
        driver = self.driver
        home = HomePage(driver)  # Initialize home page object

        home.click_dashboard_title()  # Click dashboard heading
        home.click_profile_dropdown()  # Open profile dropdown
        home.click_logout_button()  # Click logout button

        # login = LoginPage(driver)  # Optionally reinitialize login page (commented)
