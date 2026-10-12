# Pre-Entrega Automation Testing – SauceDemo

Proyecto de automatización de pruebas E2E sobre [saucedemo.com](https://www.saucedemo.com/), una aplicación web demo diseñada para prácticas de testing. Desarrollado como pre-entrega del curso de **Automatización QA**.

---

## 📌 Propósito del proyecto

Aplicar los conocimientos adquiridos en el curso para automatizar flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**, demostrando capacidad para:

- Interactuar con elementos web.
- Aplicar estrategias de localización (ID, Class Name, CSS Selector).
- Validar estados de la interfaz (URLs, títulos, presencia de elementos).
- Estructurar un proyecto de testing mantenible y escalable.

Los casos de prueba automatizados cubren:

1. **Login** con credenciales válidas y validación de redirección.
2. **Verificación del catálogo** de productos (título, presencia de items, nombre y precio).
3. **Interacción con el carrito**: agregar producto, verificar contador y confirmar que aparece en el carrito.

---

## 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3.11** | Lenguaje principal |
| **Pytest** | Framework de testing |
| **Selenium WebDriver** | Automatización del navegador |
| **webdriver-manager** | Gestión automática del ChromeDriver |
| **pytest-html** | Generación de reportes HTML |
| **Git / GitHub** | Control de versiones |

---

## 📂 Estructura del proyecto

```
pre-entrega-automation-testing-[nombre-apellido]/
│
├── tests/
│   └── test_saucedemo.py        # Casos de prueba automatizados
│
├── utils/
│   └── helpers.py               # Funciones auxiliares (esperas, screenshots, etc.)
│
├── reports/                     # Reportes HTML y capturas de pantalla
│   └── .gitkeep
│
├── conftest.py                  # Fixtures de pytest (driver, hooks de captura)
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación de dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/ailuni12/pre-entrega-automation-testing-ailin-nicliz.git
cd pre-entrega-automation-testing-ailin-nicliz
```

### 2. Crear y activar un entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:
```
pytest
pytest-html
selenium
webdriver-manager
```

> ⚠️ Asegurate de tener **Google Chrome** instalado. `webdriver-manager` descarga automáticamente la versión correcta de ChromeDriver.

---

## ▶️ Ejecución de las pruebas

### Ejecutar todos los tests

```bash
pytest -v
```

### Ejecutar con reporte HTML

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

### Ejecutar un test específico

```bash
pytest tests/test_saucedemo.py::test_01_login -v
```

### Ejecutar generando capturas automáticas en caso de fallo

Las capturas se guardan automáticamente en `reports/` cuando un test falla (configurado en `conftest.py`).

---

## 🧪 Casos de prueba implementados

| ID | Test | Descripción | Validaciones |
|---|---|---|---|
| TC-01 | `test_01_login` | Login con `standard_user` / `secret_sauce` | Redirección a `/inventory.html` |
| TC-02 | `test_02_verificar_inventario` | Verificación del catálogo | Título `Swag Labs` y sección `Products` |
| TC-03 | `test_03_verificar_inventario` | Presencia y contenido de productos | Al menos 1 item y primer nombre = `Sauce Labs Backpack` |
| TC-04 | `test_04_validar_interfaz` | Validación de UI | Menú lateral y filtro visibles |
| TC-05 | `test_05_agregar_carrito` | Agregar primer producto | El botón cambia a `Remove` |
| TC-06 | `test_06_contador_carrito` | Verificar contador del carrito | Badge del carrito = `1` |
| TC-07 | `test_07_navegar_carrito` | Navegar al carrito | Redirección a `/cart.html` |
| TC-08 | `test_08_comprobar_producto_carrito` | Verificar producto en el carrito | El item agregado aparece en el carrito |

---

## 🔄 Orden de ejecución

Los tests están pensados para correr **en orden secuencial** dentro de una misma sesión de navegador (fixture `driver` con `scope="module"`), simulando un flujo real de usuario:

```
Login → Catálogo → UI → Agregar al carrito → Contador → Ir al carrito → Verificar producto
```

Cada test valida un paso del flujo, y los asserts están redactados con mensajes claros que indican qué se esperaba y qué se obtuvo.

---

## 📊 Reporte de resultados

El reporte HTML se genera en `reports/reporte_preentrega.html` y puede abrirse directamente en el navegador. Incluye:

- Estado de cada test (pass / fail / skip).
- Duración de ejecución.
- Detalle de fallos con traceback.
- Capturas de pantalla asociadas a fallos (si aplica).

---

## Evidencias

- **Capturas automáticas:** en `reports/FAIL_*.png` cuando un test falla.
- **Logs de ejecución:** salida de la consola al correr `pytest -v`.

---

## 📝 Buenas prácticas aplicadas

- Uso de **esperas explícitas** (`WebDriverWait` + `expected_conditions`) para evitar fallos por timing.
- **Fixtures de pytest** con `scope="module"` para reutilizar el driver.
- Tests **independientes** entre sí: cada test valida su propio flujo.
- Separación de **código de test** (`tests/`) y **funciones auxiliares** (`utils/`).
- Nomenclatura descriptiva para tests, funciones y variables.
- Comentarios explicativos en los puntos clave del código.

---

## 👤 Autor

**Ailin Nicliz**
Curso: Automatización QA – Talento Tech 2026
Repositorio: [https://github.com/ailuni12/pre-entrega-automation-testing-ailin-nicliz](https://github.com/ailuni12/pre-entrega-automation-testing-ailin-nicliz)

---

## Licencia

Proyecto con fines educativos.
