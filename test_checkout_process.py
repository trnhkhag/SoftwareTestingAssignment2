import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

# TC1: Test Checkout with empty first name
def test_checkout_empty_first_name(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "last-name").send_keys("Tran")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    text = driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3').text
    assert "Error: First Name is required" in text

# TC2: Test Checkout with empty last name
def test_checkout_empty_last_name(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Khang")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    text = driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3').text
    assert "Error: Last Name is required" in text

# TC3: Test Checkout with empty post code
def test_checkout_empty_post_code(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Khang")
    driver.find_element(By.ID, "last-name").send_keys("Tran")
    driver.find_element(By.ID, "continue").click()
    text = driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3').text
    assert "Error: Postal Code is required" in text

# TC4: Test Checkout with valid inputs
def test_checkout_valid_inputs(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Khang")
    driver.find_element(By.ID, "last-name").send_keys("Tran")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
    assert "Checkout: Complete!" in text