from pages.login_page import LoginPage
from pages.pim_page import PimPage


def test_add_employee(driver):
    login = LoginPage(driver)
    login.login()

    pim = PimPage(driver)
    pim.go_to_pim()
    pim.add_employee("Akshaya", "Test", "12345")



