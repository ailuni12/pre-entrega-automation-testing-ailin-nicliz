import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()

def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    assert "/inventory.html"in driver.current_url, "ERROR: No se redirigio a /inventory.html"

def test_02_verificar_inventario(driver):
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME,"title").text

    assert page_title == "Swag Labs", f"ERROR: Titulo esperado: 'Swag Labs'; Titulo obtenido: '{page_title}'"
    assert section_title == 'Products', f"ERROR: Titulo esperado: 'Products'; Titulo obtenido: '{section_title}'"

def test_03_verificar_inventario(driver):
    inventory_list = driver.find_elements(By.CLASS_NAME,"inventory_item")
    item_name = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    
    assert len(inventory_list) > 0, f'ERROR: No se encontraror items'
    assert item_name == "Sauce Labs Backpack", f'ERROR: Esperado: "Sauce Labs Backpack", obtenido: "{item_name}"'

def test_04_validar_interfaz(driver):
    menu_button = driver.find_element(By.ID,"react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME,"product_sort_container")

    assert menu_button.is_displayed(), f'ERROR: El menu no se visualiza al hacer click'
    assert filtro.is_displayed(), f'ERROR: El filtro no se visualiza al hacer click'

def test_05_agregar_carrito(driver):
    item = driver.find_elements(By.CLASS_NAME,"inventory_item")[0]
    boton_agregar = item.find_element(By.TAG_NAME,"button")
    boton_agregar.click()

    assert boton_agregar.text.capitalize() == "Remove", f'ERROR: El boton no cambio a Remove'

def test_06_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text

    assert contador_carrito == "1", f'ERROR: se esperaba "1", se obtuvo "{contador_carrito}"'

def test_07_navegar_carrito(driver):
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    assert "/cart.html"in driver.current_url, "ERROR: No se redirigio a /cart.html"

def test_08_comprobar_producto_carrito(driver):
    item_carrito = driver.find_element(By.CLASS_NAME,"inventory_item_name").text

    assert item_carrito == "Sauce Labs Backpack", f'ERROR: Esperado: "Sauce Labs Backpack", obtenido: "{item_carrito}"'