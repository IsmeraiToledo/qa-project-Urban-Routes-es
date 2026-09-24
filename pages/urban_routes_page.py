from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, 'button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')


    # Paso 1. Localizar el elemento
    # Buscamos el elemento en la pantalla.
    # Identificamos su etiqueta y atributos.
    # Crear un nombre que haga sentido con el tipo de elemento y su accion.
    # Crear una variable de tipo Tupla con un nombre que indique que tipo de elemento es:
    # request_taxi_button = (By.CSS.SELECTOR, 'button.round')

    # Paso 2. Obtener el elemento. GETTER
    # Copio el nombre del localizador del elemento y creo un nuevo metodo llamado get_nombre_del_elemento():
    #     def get_request_taxi_button(self):
    #         return self.wait.until(
    #             EC.element_to_be_clickable(self.request_taxi_button)
    #             )

    # Paso 3. Realizar la accion con el elemento.
    # SETTER -> Campos de textos y se usa con el metodo send_keys()     set_nombre_del_elemento():
    # CLICKER -> Cuando es un boton o un link o quiero hacer un click en cualquier elemento y uso el metodo
    # clic () click_nombre_del_elemento():
    # READER -> Cuando quiero leer alguna propiedad como el valor de un elemento para usarlo en un assert uso el metodo
    # get_property('value') o el metodo .text       read_nombre_del_elemento():


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
            )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )
    def reader_comfort_icon_assert(self):
        comfort_tariff = self.get_comfort_icon_assert().text
        return comfort_tariff