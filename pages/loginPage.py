from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Element locators
        self.username_textbox_NAME = "username"
        self.password_textbox_NAME = "password"
        self.login_button_CSS = "button[type='submit']"  # Correct CSS selector

    # Generic wait helper
    def wait_for_element(self, by_locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(by_locator)
        )

    # Page actions
    def enter_username(self, username):
        element = self.wait_for_element((By.NAME, self.username_textbox_NAME))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait_for_element((By.NAME, self.password_textbox_NAME))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        element = self.wait_for_element((By.CSS_SELECTOR, self.login_button_CSS))
        element.click()

    def is_login_page_visible(self):
        return self.wait_for_element((By.NAME, self.username_textbox_NAME)).is_displayed()
