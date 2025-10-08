from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Element locators
        self.dashboard_title_XPATH = "//h6[normalize-space()='Dashboard']"
        self.profile_dropdown_XPATH = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logout_button_XPATH = "//a[normalize-space()='Logout']"

    # Generic wait helper
    def wait_for_element(self, by_locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(by_locator)
        )

    # Page actions
    def click_dashboard_title(self):
        element = self.wait_for_element((By.XPATH, self.dashboard_title_XPATH))
        element.click()

    def click_profile_dropdown(self):
        element = self.wait_for_element((By.XPATH, self.profile_dropdown_XPATH))
        element.click()

    def click_logout_button(self):
        element = self.wait_for_element((By.XPATH, self.logout_button_XPATH))
        element.click()

    # Simple assertion helper
    def is_dashboard_visible(self):
        return self.wait_for_element((By.XPATH, self.dashboard_title_XPATH)).is_displayed()