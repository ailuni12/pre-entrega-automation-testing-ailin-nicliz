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
    


