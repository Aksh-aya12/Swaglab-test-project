from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PimPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # -----------------------------
    # Wait until loading spinner disappears
    def wait_loader_disappear(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, ".oxd-loading-spinner")
                )
            )
        except TimeoutException:
            pass

    # -----------------------------
    # Navigate to PIM menu
    def go_to_pim(self):
        pim = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        )
        pim.click()
        self.wait_loader_disappear()

    # -----------------------------
    # Add employee
    def add_employee(self, first, last, emp_id):

        # Click Add Employee
        click_add_emp = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Add Employee']")
            )
        )
        click_add_emp.click()

        # First name
        firstname = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "firstName"))
        )
        firstname.send_keys(first)

        # Last name
        lastname = self.driver.find_element(By.NAME, "lastName")
        lastname.send_keys(last)

        # Employee ID (more specific locator)
        employee_id = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//input[contains(@class,'oxd-input')])[3]")
            )
        )
        employee_id.clear()
        employee_id.send_keys(emp_id)

        # Save
        submit = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        )
        submit.click()

        self.wait_loader_disappear()
    # -----------------------------









