import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome browser instance with Service
def initialize_driver():
    return webdriver.Chrome()

# Function to find the input element associated with a label
def find_input_by_label(driver, label_text, wait_time=10):
    try:
        label = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, f"//label[text()='{label_text}']"))
        )
        input_id = label.get_attribute("for")
        input_field = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, input_id))
        )
        return input_field
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error finding input for '{label_text}': {e}")
        return None

# Function to insert text into an input field
def insert_text_into_input(input_field, text):
    try:
        if input_field.is_enabled() and input_field.is_displayed():
            input_field.clear()
            input_field.send_keys(text)
            print(f"Inserted text into field: {text}")
        else:
            print("Input field is not interactable")
    except ElementNotInteractableException as e:
        print(f"Error inserting text: {e}")

# Function to find and click a button by its text
def click_button(driver, button_text, wait_time=10):
    try:
        button = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']"))
        )
        button.click()
        print(f"Clicked button: {button_text}")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error clicking button '{button_text}': {e}")

# Function to verify the current URL
def verify_url(driver, expected_url):
    current_url = driver.current_url
    if current_url == expected_url:
        print(f"Successfully navigated to: {current_url}")
    else:
        print(f"Navigation failed. Current URL: {current_url}, Expected URL: {expected_url}")

# Function to find and click the "Logout" link
def find_and_click_logout(driver, logout_text="Log out", wait_time=10):
    try:
        logout_link = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, logout_text))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", logout_link)
        logout_link.click()
        print(f"Clicked link: {logout_text}")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error clicking '{logout_text}' link: {e}")
        elements = driver.find_elements(By.PARTIAL_LINK_TEXT, logout_text)
        if elements:
            for element in elements:
                print(f"Element displayed: {element.is_displayed()}, enabled: {element.is_enabled()}")
        else:
            print(f"No elements found with link text '{logout_text}'")

# Function to verify we are redirected back to the login page
def check_return_to_login_page(driver, login_page_url):
    current_url = driver.current_url
    if current_url == login_page_url:
        print(f"Returned to login page: {current_url}")
    else:
        print(f"Failed to return to login page. Current URL: {current_url}, Expected URL: {login_page_url}")

# Function to check for error messages
def check_for_error_message(driver, wait_time=10):
    try:
        # Wait for the error message to appear
        error_message_element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "error"))
        )
        if "show" in error_message_element.get_attribute("class"):
            error_message = error_message_element.text
            print(f"Error message found: {error_message}")
            return error_message
        else:
            print("Error message element is present but not visible.")
            return None
    except TimeoutException:
        print("No error message found.")
        return None

# Function to perform the login action and handle different outcomes
def perform_login_test(driver, username, password, expected_dashboard_url, expected_error_message=None):
    # Find and interact with the Username input field
    username_input = find_input_by_label(driver, "Username")
    if username_input:
        insert_text_into_input(username_input, username)
    
    # Find and interact with the Password input field
    password_input = find_input_by_label(driver, "Password")
    if password_input:
        insert_text_into_input(password_input, password)

    # Click the Submit button
    click_button(driver, "Submit")

    # Wait briefly to allow for page transitions
    time.sleep(5)

    # Check for error messages if expected
    if expected_error_message:
        actual_error_message = check_for_error_message(driver)
        if actual_error_message and expected_error_message in actual_error_message:
            print(f"Expected error message received: {actual_error_message}")
        else:
            print(f"Error: Expected '{expected_error_message}', but got '{actual_error_message}'")
    else:
        # Verify the new URL matches the expected dashboard URL
        verify_url(driver, expected_dashboard_url)

# Main function to perform the sequence of actions for multiple test scenarios
def main():
    login_url = "https://practicetestautomation.com/practice-test-login/"  
    expected_dashboard_url = "https://practicetestautomation.com/logged-in-successfully/"  
    login_page_url = login_url  # The URL to return to after logging out

    # Initialize the WebDriver
    driver = initialize_driver()

    try:
        # Open the login URL
        driver.get(login_url)

        # Define test scenarios
        test_scenarios = [
            {"username": "student", "password": "Password123", "expected_error_message": None},
            {"username": "incorrectUser", "password": "Password123", "expected_error_message": "Your username is invalid!"},
            {"username": "student", "password": "incorrectPassword", "expected_error_message": "Your password is invalid!"}
        ]

        for scenario in test_scenarios:
            print(f"\nTesting with username: {scenario['username']}, password: {scenario['password']}")
            login_successful = perform_login_test(
                driver,
                scenario['username'],
                scenario['password'],
                expected_dashboard_url,
                scenario['expected_error_message']
            )

            # If login was successful, check for logout
            if login_successful:
                print("Login successful, performing logout test.")
                find_and_click_logout(driver, "Log out")
                check_return_to_login_page(driver, login_page_url)
            else:
                print("Login failed or was intended to fail, no logout test performed.")

            # Reset to the login page for the next test
            driver.get(login_url)
            time.sleep(3)

    finally:
        # Always close the browser at the end
        driver.quit()


# Run the main function
if __name__ == "__main__":
    main()
