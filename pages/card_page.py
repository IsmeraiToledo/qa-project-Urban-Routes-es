from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CardPage:
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, 'input#code.card-input')
    payment_method_button = (
        By.XPATH,
        '//div[contains(@class, "pp-button")][.//div[text()="Método de pago"]]'
    )
    add_card_button = (
        By.XPATH,
        '//div[contains(@class, "pp-row")][.//div[text()="Agregar tarjeta"]]'
    )
    add_button = (By.XPATH, '//button[text()="Agregar"]')
    card_assert = (
        By.XPATH,
        '//div[contains(@class, "pp-row")][.//*[text()="Tarjeta"]]'
    )
    close_payment_button = (
        By.CSS_SELECTOR,
        '.payment-picker.open .section.active .section-close'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_card_code_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        )

    def set_card_code(self, card_code):
        card_code_field = self.get_card_code_field()
        card_code_field.send_keys(card_code)
        card_code_field.send_keys(Keys.TAB)

    def get_payment_method_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.payment_method_button)
        )

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        )

    def set_card_number(self, card_number):
        self.get_card_number_field().send_keys(card_number)

    def get_add_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_add_button(self):
        self.get_add_button().click()

    def get_card_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_assert)
        )

    def reader_card_assert(self):
        return self.get_card_assert().text

    def get_close_payment_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.close_payment_button)
        )

    def click_close_payment_button(self):
        self.get_close_payment_button().click()