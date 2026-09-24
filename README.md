# Proyecto Urban Routes

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para la aplicación Urban Routes.

El objetivo es comprobar el proceso completo para solicitar un taxi, incluyendo:

- Configurar las direcciones de origen y destino.
- Seleccionar la tarifa Comfort.
- Agregar un número de teléfono.
- Agregar una tarjeta de crédito.
- Escribir un mensaje para el conductor.
- Solicitar manta y pañuelos.
- Solicitar dos helados.
- Pedir un taxi.
- Comprobar que aparece el modal de búsqueda de automóvil.
- Esperar a que aparezca la información del conductor.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- PyCharm
- Git y GitHub

## Técnicas utilizadas

El proyecto utiliza el patrón Page Object Model para separar los localizadores y métodos de las pruebas.

Los Page Objects están organizados en diferentes archivos:

- `urban_routes_page.py`: configuración de ruta y selección de tarifa.
- `phone_page.py`: ingreso y confirmación del número de teléfono.
- `card_page.py`: configuración del método de pago y tarjeta.
- `order_page.py`: mensaje para el conductor, requisitos del pedido, helados y solicitud del taxi.

También se utilizan esperas explícitas con `WebDriverWait` y `expected_conditions`.

## Cómo ejecutar las pruebas

1. Abrir el proyecto en PyCharm.

2. Instalar las dependencias:

```bash
pip install pytest selenium
```
3. Verificar que la URL de Urban Routes en data/data.py esté actualizada.
4. Ejecutar todas las pruebas
```bash 
pytest tests/test_urban_routes.py
```