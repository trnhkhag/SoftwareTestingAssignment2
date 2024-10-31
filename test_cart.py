import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
# TC1: Test view cart
def test_view_cart(driver):
    login(driver)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    assert "cart.html" in driver.current_url    

# TC2: Test add single product to cart
def test_add_single_product(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_quantity = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    cart_quantity = int(cart_quantity)
    assert cart_quantity == 1
    
# TC3: Test add multiple product to cart
def test_add_multiple_products(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    cart_quantity = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    cart_quantity = int(cart_quantity)
    assert cart_quantity == 4
    
# TC4: Test remove single product from cart
def test_remove_single_product(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    hasProduct = True
    try:
        driver.find_element(By.CLASS_NAME, "cart_item")
    except NoSuchElementException:
        hasProduct = False
    assert hasProduct == False
    
# TC5: Test remove multiple products from cart
def test_remove_multiple_products(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    cart_quantity = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    cart_quantity = int(cart_quantity)
    assert cart_quantity == 2
    
# TC6: Test add product to cart from product detail
def test_add_product_from_product_detail(driver):
    login(driver)
    driver.find_element(By.ID, "item_4_title_link").click()
    driver.find_element(By.ID, "add-to-cart").click()
    cart_quantity = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    cart_quantity = int(cart_quantity)
    assert cart_quantity == 1