from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:
    message_for_driver_field = (By.ID, 'comment')
    blanket_and_tissues_checkbox = (
        By.XPATH,
        '//div[contains(@class, "r-sw-container")]'
        '[.//div[text()="Manta y pañuelos"]]'
        '//input[@type="checkbox"]'
    )

    blanket_and_tissues_switch = (
        By.XPATH,
        '//div[contains(@class, "r-sw-container")]'
        '[.//div[text()="Manta y pañuelos"]]'
        '//span[contains(@class, "slider")]'
    )

    ice_cream_plus_button = (
        By.XPATH,
        '//div[contains(@class, "r-counter-container")]'
        '[.//div[text()="Helado"]]'
        '//div[contains(@class, "counter-plus")]'
    )

    ice_cream_count = (
        By.XPATH,
        '//div[contains(@class, "r-counter-container")]'
        '[.//div[text()="Helado"]]'
        '//div[contains(@class, "counter-value")]'
    )

    final_request_taxi_button = (
        By.XPATH,
        '//button[contains(@class, "smart-button")][.//span[text()="Pedir un taxi"]]'
    )
    search_taxi_modal_title = (
        By.XPATH,
        '//*[normalize-space()="Buscar automóvil"]'
    )
    driver_info_title = (
        By.XPATH,
        '//*[contains(normalize-space(), "El conductor llegará")]'
    )


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_message_for_driver_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.message_for_driver_field)
        )

    def set_message_for_driver(self, message):
        self.get_message_for_driver_field().send_keys(message)

    def reader_message_for_driver(self):
        return self.get_message_for_driver_field().get_property('value')

    def get_blanket_and_tissues_switch(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.blanket_and_tissues_switch)
        )

    def click_blanket_and_tissues(self):
        self.get_blanket_and_tissues_switch().click()

    def get_blanket_and_tissues_checkbox(self):
        return self.wait.until(
            EC.presence_of_element_located(self.blanket_and_tissues_checkbox)
        )

    def is_blanket_and_tissues_selected(self):
        return self.get_blanket_and_tissues_checkbox().is_selected()

    def get_ice_cream_plus_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_plus_button)
        )

    def click_ice_cream_plus_button(self):
        self.get_ice_cream_plus_button().click()

    def get_ice_cream_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ice_cream_count)
        )

    def reader_ice_cream_count(self):
        return self.get_ice_cream_count().text

    def get_final_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.final_request_taxi_button)
        )

    def click_final_request_taxi_button(self):
        self.get_final_request_taxi_button().click()

    def get_search_taxi_modal_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.search_taxi_modal_title)
        )

    def reader_search_taxi_modal_title(self):
        return self.get_search_taxi_modal_title().text

    def get_driver_info_title(self):
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.driver_info_title)
        )

    def reader_driver_info_title(self):
        return self.get_driver_info_title().text