import pytest
import re
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
    
# TC1: Test total price presentation of single product
def test_total_price_single_product(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Khang")
    driver.find_element(By.ID, "last-name").send_keys("Tran")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    text = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
    match = re.search(r"\d+\.\d+", text)
    if match:
        total = float(match.group())
    assert total == 29.99
    
# TC2: Test total price presentation of multiple products
def test_total_price_multiple_products(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Khang")
    driver.find_element(By.ID, "last-name").send_keys("Tran")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    text = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
    match = re.search(r"\d+\.\d+", text)
    if match:
        total = round(float(match.group()), 2)
    assert total == 105.96