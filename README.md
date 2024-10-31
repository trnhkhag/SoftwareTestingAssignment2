# Automated Testing with Selenium and Pytest

This project contains automated test cases using **Selenium WebDriver** and **Pytest** to validate the sorting functionality on the [Sauce Demo](https://www.saucedemo.com/) website.

## Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Tests](#running-the-tests)
- [Test Cases](#test-cases)
- [Notes](#notes)

---

## Requirements

### 1. Software
- **Python**: Version 3.7 or higher
- **Browser**: Microsoft Edge (or modify for Chrome, Firefox, etc.)
- **Edge WebDriver**: Match the version of your Edge browser (instructions below).

### 2. Python Libraries
- **Selenium**: For browser automation
- **Pytest**: For running and managing test cases

---

## Setup Instructions

### 1. Install Python
1. [Download Python](https://www.python.org/downloads/) and install it, ensuring the option to "Add Python to PATH" is checked during installation.
2. Verify the installation by running:
   ```bash
   python --version
   ```

### 2. Install Required Python Packages
Use `pip` to install Selenium and Pytest:
   ```bash
   pip install selenium pytest
   ```

### 3. Set Up Edge WebDriver
To automate tests with Microsoft Edge:
1. Find your **Microsoft Edge** version by going to `edge://settings/help`.
2. Download the matching **Edge WebDriver** version from [Microsoft's official WebDriver site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
3. Extract the WebDriver executable (e.g., `msedgedriver.exe`) and place it in a directory included in your **system PATH**, or update the `driver` fixture to point to the exact path of the driver file.

Alternatively, if using **Chrome**:
- Replace `webdriver.Edge()` with `webdriver.Chrome()` in the script, and download **ChromeDriver** instead.

### 4. Test Environment Configuration
1. Ensure a stable internet connection, as the tests interact with the online [Sauce Demo](https://www.saucedemo.com/) site.
2. Confirm that the account credentials used (`standard_user` and `secret_sauce`) are functional on the test site.

---

## Running the Tests

### Command Line Execution
To execute all tests, navigate to the project directory and run:
   ```bash
   pytest <your_script_name>.py
   ```

### Pytest Options
- **-v**: Increase verbosity to display each test case.
- **--html=report.html**: Generate an HTML report for the test run.

Example:
   ```bash
   pytest -v --html=report.html
   ```

### Sample Test Execution Command
In the terminal, run the following command to see detailed output and generate a report:
   ```bash
   pytest test_sauce_demo.py -v --html=report.html
   ```

## Test Cases

This project includes four test cases for sorting products on the Sauce Demo website:

1. **Test Sort Product by Name in Ascending Order**  
   - Verifies that products are sorted by name (A-Z).

2. **Test Sort Product by Name in Descending Order**  
   - Verifies that products are sorted by name (Z-A).

3. **Test Sort Product by Price in Ascending Order**  
   - Verifies that products are sorted by price from lowest to highest.

4. **Test Sort Product by Price in Descending Order**  
   - Verifies that products are sorted by price from highest to lowest.

Each test case includes login automation and sorting validation, checking if the expected order matches the actual order displayed on the site.

---

## Notes
- The Edge WebDriver version must match the installed Edge browser version to prevent compatibility issues.
- Modify the `login` function if credentials or elements on the page change.
- Additional configuration may be required if running on CI/CD pipelines or virtual environments.

---

This guide covers setup, test execution, and environment requirements for running the automated test cases. Happy Testing!
