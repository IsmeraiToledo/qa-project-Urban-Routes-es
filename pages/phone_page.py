from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PhonePage:

    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_number_field = (By.ID, 'phone')
    phone_code_field = (By.ID, 'code')
    next_button = (By.XPATH, '//button[text()="Siguiente"]')
    confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    phone_number_assert = (By.CSS_SELECTOR, '.np-button .np-text')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_field)
        )

    def set_phone_number(self, phone_number):
        self.get_phone_number_field().send_keys(phone_number)

    def get_phone_code_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_code_field)
        )

    def set_phone_code(self, phone_code):
        self.get_phone_code_field().send_keys(phone_code)

    def get_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_next_button(self):
        self.get_next_button().click()

    def get_confirm_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.confirm_button)
        )

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def get_phone_number_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_assert)
        )

    def reader_phone_number_assert(self):
        phone_number = self.get_phone_number_assert().text
        return phone_number