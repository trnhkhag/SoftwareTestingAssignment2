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
    
# TC1: Test navigate from inventory page to cart page
def test_navigate_inventory_to_cart(driver):
    login(driver)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    assert "cart.html" in driver.current_url
    
# TC2: Test navigate from inventory page to product detail page
def test_navigate_inventory_to_product_detail(driver):
    login(driver)
    driver.find_element(By.ID, "item_4_title_link").click()
    assert "inventory-item.html?id=4" in driver.current_url
    
# TC3: Test navigate from cart page to checkout page
def test_navigate_cart_to_checkout(driver):
    login(driver)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    assert "checkout-step-one.html" in driver.current_url
    
# TC4: Test navigate from product detail page to inventory page
def test_navigate_product_detail_to_inventory(driver):
    login(driver)
    driver.find_element(By.ID, "item_4_title_link").click()
    driver.find_element(By.ID, "back-to-products").click()
    assert "inventory.html" in driver.current_url
    
# TC5: Test navigate from cart page to inventory page
def test_navigate_cart_to_inventory(driver):
    login(driver)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "continue-shopping").click()
    assert "inventory.html" in driver.current_url