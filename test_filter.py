import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

# TC1: Test sort product by name in ascending order
def test_sort_product_by_name_ascending(driver):
    login(driver)
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    actual_product_list = []
    for p in products:
        actual_product_list.append(p.text)
    assert expected_product_list == actual_product_list

# TC2: Test sort product by name in descending order
def test_sort_product_by_name_descending(driver):
    login(driver)
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').click()
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    expected_product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    expected_product_list = sorted(expected_product_list, reverse=True)
    actual_product_list = []
    for p in products:
        actual_product_list.append(p.text)
    assert expected_product_list == actual_product_list
    
# TC3: Test sort product by price in ascending order
def test_sort_product_by_price_ascending(driver):
    login(driver)
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').click()
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    expected_price_list = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]
    actual_price_list = []
    for p in prices:
        actual_price_list.append(float(p.text[1:]))
    assert expected_price_list == actual_price_list
    
# TC4: Test sort product by price in descending order
def test_sort_product_by_price_descending(driver):
    login(driver)
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    expected_price_list = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]
    expected_price_list = sorted(expected_price_list, reverse=True)
    actual_price_list = []
    for p in prices:
        actual_price_list.append(float(p.text[1:]))
    assert expected_price_list == actual_price_list