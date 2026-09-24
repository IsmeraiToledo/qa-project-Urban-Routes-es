from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage
from pages.phone_page import PhonePage
from utils.retrive_code import retrieve_phone_code
from pages.card_page import CardPage
from pages.order_page import OrderPage


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)

        self.routes_page = UrbanRoutesPage(self.driver)
        self.phone_page = PhonePage(self.driver)
        self.card_page = CardPage(self.driver)
        self.order_page = OrderPage(self.driver)

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        assert self.routes_page.reader_comfort_icon_assert() == "Comfort"

    def test_3_add_phone_number(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)
        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        assert self.phone_page.reader_phone_number_assert() == phone_number

    def test_4_add_credit_card(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()

        assert "Tarjeta" in self.card_page.reader_card_assert()
        self.card_page.click_close_payment_button()

    def test_5_write_message_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        message_for_driver = data.message_for_driver

        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()
        self.card_page.click_close_payment_button()

        self.order_page.set_message_for_driver(message_for_driver)

        assert self.order_page.reader_message_for_driver() == message_for_driver

    def test_6_request_blanket_and_tissues(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        message_for_driver = data.message_for_driver

        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()
        self.card_page.click_close_payment_button()

        self.order_page.set_message_for_driver(message_for_driver)

        self.order_page.click_blanket_and_tissues()

        assert self.order_page.is_blanket_and_tissues_selected()

    def test_7_request_two_ice_creams(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        message_for_driver = data.message_for_driver

        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()
        self.card_page.click_close_payment_button()

        self.order_page.set_message_for_driver(message_for_driver)

        self.order_page.click_blanket_and_tissues()

        self.order_page.click_ice_cream_plus_button()
        self.order_page.click_ice_cream_plus_button()

        assert self.order_page.reader_ice_cream_count() == "2"

    def test_8_search_taxi_modal(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        message_for_driver = data.message_for_driver

        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()
        self.card_page.click_close_payment_button()

        self.order_page.set_message_for_driver(message_for_driver)

        self.order_page.click_blanket_and_tissues()

        self.order_page.click_ice_cream_plus_button()
        self.order_page.click_ice_cream_plus_button()

        assert self.order_page.reader_ice_cream_count() == "2"

        self.order_page.click_final_request_taxi_button()
        assert self.order_page.reader_search_taxi_modal_title() == "Buscar automóvil"

    def test_9_wait_for_driver_info(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        message_for_driver = data.message_for_driver

        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

        self.phone_page.click_phone_number_button()
        self.phone_page.set_phone_number(phone_number)
        self.phone_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)

        self.phone_page.set_phone_code(phone_code)
        self.phone_page.click_confirm_button()

        self.card_page.click_payment_method_button()
        self.card_page.click_add_card_button()
        self.card_page.set_card_number(card_number)
        self.card_page.set_card_code(card_code)
        self.card_page.click_add_button()
        self.card_page.click_close_payment_button()

        self.order_page.set_message_for_driver(message_for_driver)

        self.order_page.click_blanket_and_tissues()

        self.order_page.click_ice_cream_plus_button()
        self.order_page.click_ice_cream_plus_button()

        assert self.order_page.reader_ice_cream_count() == "2"

        self.order_page.click_final_request_taxi_button()

        assert "El conductor llegará" in self.order_page.reader_driver_info_title()

    def teardown_method(self):
        self.driver.quit()