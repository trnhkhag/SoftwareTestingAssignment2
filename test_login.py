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

# TC1: Valid Login
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)
    assert "inventory.html" in driver.current_url

# TC2: Invalid Login
def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message


# TC3: Empty Usernam
def test_empty_username(driver):
    driver.get("http://www.saucedemo.com/")
    driver.find_element(By.ID, "password").send_keys("12345678")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username is required" in error_message


# TC4: Empty Password
def test_empty_password(driver):
    driver.get("http://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("abc")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Password is required" in error_message

# TC5: Logout functionality
def test_logout_functionality(driver):
    driver.get("http://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    assert "https://www.saucedemo.com/" == driver.current_url