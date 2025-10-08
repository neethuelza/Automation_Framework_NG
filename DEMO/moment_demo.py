# # from datetime import datetime
# #
# # x = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
# # print(x)
#
# import inspect
#
# def whoami():
#     return inspect.stack()[1][3]


import os
from datetime import datetime

import allure
import self

from utils import utils

try:
    # your test steps...
    pass
except AssertionError as error:
    print("Assertion error occurred:", error)

    # Safe timestamp for filenames
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = utils.whoami()
    screenshot_name = f"{test_name}_{current_time}"

    # Attach to Allure
    allure.attach(
        self.driver.get_screenshot_as_png(),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG
    )

    # Ensure folder exists
    screenshot_dir = "C:/Users/abyja/PycharmProjects/Automation_Framework_NG/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Full file path
    screenshot_path = os.path.join(screenshot_dir, f"{screenshot_name}.png")

    # Save screenshot
    if self.driver.get_screenshot_as_file(screenshot_path):
        print(f"Screenshot saved to: {screenshot_path}")
    else:
        print("Failed to save screenshot!")
