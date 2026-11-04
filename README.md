# 🚕 Urban Routes
### Automatización de pruebas web · QA Engineering · TripleTen

Pruebas automatizadas del flujo de solicitud de un taxi en Urban Routes con **Python, pytest y Selenium WebDriver**.

**9 pruebas automatizadas** · **Selenium WebDriver** · **Page Object Model**

---

## 🎯 Objetivo

Comprobar el flujo de solicitud de un taxi con tarifa Comfort, desde la configuración de la ruta hasta la aparición del mensaje de llegada del conductor.

Las pruebas verifican los datos ingresados, las opciones seleccionadas y los mensajes mostrados durante la solicitud.

## 🛠️ Herramientas y técnicas

- **Python y pytest:** desarrollo y ejecución de pruebas.
- **Selenium WebDriver:** interacción automatizada con el navegador.
- **Google Chrome:** navegador utilizado para las pruebas.
- **Page Object Model:** organización de las interacciones mediante clases por funcionalidad.
- **Funciones auxiliares:** recuperación del código de confirmación del teléfono.
- **Git y GitHub:** control de versiones y documentación del proyecto.

## 🔎 Cobertura de pruebas

| Prueba | Comprobación |
|---|---|
| Configurar ruta | Las direcciones de origen y destino coinciden con las ingresadas |
| Seleccionar tarifa | La tarifa seleccionada muestra “Comfort” |
| Confirmar teléfono | El número mostrado coincide con el ingresado |
| Agregar tarjeta | El método de pago muestra “Tarjeta” |
| Escribir mensaje | El texto coincide con el mensaje ingresado |
| Solicitar manta y pañuelos | La opción queda seleccionada |
| Solicitar helados | El contador muestra 2 |
| Solicitar taxi | El modal muestra “Buscar automóvil” |
| Consultar asignación | El título contiene “El conductor llegará” |

## 🔄 Preparación y cierre

Cada prueba inicia una sesión nueva de Chrome y abre la aplicación con la URL configurada.

Los escenarios realizan los pasos previos necesarios antes de ejecutar su comprobación. Las pruebas posteriores incluyen acciones como configurar la ruta, seleccionar Comfort, confirmar el teléfono y agregar una tarjeta.

Para confirmar el teléfono, se utiliza la función auxiliar `retrieve_phone_code`. El navegador se configura con registros de rendimiento habilitados.

Al finalizar cada prueba, la sesión del navegador se cierra mediante `driver.quit()`.

## 👩‍💻 Mi contribución

Implementé nueve pruebas automatizadas para comprobar las funcionalidades del flujo de solicitud de taxi.

Organicé las interacciones mediante Page Objects para la ruta, el teléfono, la tarjeta y las opciones del pedido. Incorporé comprobaciones de los datos ingresados, las selecciones realizadas y los mensajes mostrados por la aplicación.

## 📂 Estructura del proyecto

| Carpeta | Contenido |
|---|---|
| `data/` | URL de la aplicación y datos utilizados en las pruebas |
| `pages/` | Page Objects con métodos de interacción y consulta |
| `tests/` | Pruebas automatizadas del flujo de solicitud |
| `utils/` | Funciones auxiliares |

### Organización de los archivos

| Archivo | Responsabilidad |
|---|---|
| `data/data.py` | Datos de ruta, teléfono, tarjeta, mensaje y URL |
| `pages/urban_routes_page.py` | Configuración de ruta y selección de tarifa |
| `pages/phone_page.py` | Ingreso y confirmación del teléfono |
| `pages/card_page.py` | Configuración del método de pago |
| `pages/order_page.py` | Mensaje, complementos, helados y solicitud del taxi |
| `utils/retrive_code.py` | Función auxiliar para recuperar el código del teléfono |
| `tests/test_urban_routes.py` | Nueve pruebas y preparación y cierre del navegador |

## ▶️ Cómo ejecutar las pruebas

### 1. Clonar el repositorio

```bash
git clone https://github.com/IsmeraiToledo/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

### 2. Preparar el entorno

Tener Python y Google Chrome instalados.

Instalar las dependencias:

```bash
pip install pytest selenium
```

El código inicia Chrome mediante `webdriver.Chrome` y `Service()`, sin especificar una ruta manual de ChromeDriver. El entorno debe permitir resolver un controlador compatible con el navegador.

### 3. Configurar los datos

Actualizar la URL de Urban Routes en `data/data.py`.

Revisar que los datos de prueba estén disponibles:

- Dirección de origen.
- Dirección de destino.
- Número de teléfono.
- Número y código de tarjeta de prueba.
- Mensaje para el conductor.

La aplicación debe estar activa y accesible antes de ejecutar las pruebas.

### 4. Ejecutar las pruebas

Desde la carpeta principal del proyecto:

```bash
pytest -v tests/test_urban_routes.py
```

## 📋 Alcance y resultados

La suite contiene **9 pruebas automatizadas** del flujo de solicitud de taxi con tarifa Comfort.

Las comprobaciones cubren datos ingresados, opciones seleccionadas, búsqueda del automóvil y aparición del mensaje de llegada del conductor.

Los resultados de aprobación o fallo deben confirmarse ejecutando las pruebas contra un entorno activo.

---

Desarrollado por **Ismerai Toledo Contreras** durante su formación en QA Engineering en **TripleTen**.
