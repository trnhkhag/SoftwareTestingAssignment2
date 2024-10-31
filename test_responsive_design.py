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
    
# TC1: Test responsive on phone
def test_responsive_phone(driver):
    driver.set_window_size(375, 667)
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    actual_product_list = []
    for p in products:
        actual_product_list.append(p.text)
    assert expected_product_list == actual_product_list
    
# TC2: Test responsive on tablet
def test_responsive_tablet(driver):
    driver.set_window_size(768, 1024)
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    actual_product_list = []
    for p in products:
        actual_product_list.append(p.text)
    assert expected_product_list == actual_product_list
    
# TC3: Test responsive on desktop
def test_responsive_desktop(driver):
    driver.set_window_size(1920, 1080)
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    actual_product_list = []
    for p in products:
        actual_product_list.append(p.text)
    assert expected_product_list == actual_product_list