import sys
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAccesstest1(unittest.TestCase):
    def setUp(self):
        # Creates an instance of the Chrome WebDriver
        self.driver = webdriver.Chrome()
        # Initializes empty dictionary to store variables
        self.vars = {}
        # Create WebDriverWait instasnce with 10 second timeout
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        # Closes the browser and terminates the Web Session
        self.driver.quit()

    #  Scopus Web Link
    def test_accesstest1(self):
        # Define the variable imported from user input
        student_id = sys.argv[1]
        password = sys.argv[2]
        query = sys.argv[3]
        startyear = sys.argv[4]
        endyear = sys.argv[5]

        # Tells the Robot to Access the Scopus Website and Maximise the Window Size
        self.driver.get("https://www.scopus.com/home.uri?zone=header&origin=")
        self.driver.maximize_window()

        time.sleep(1)  # Adds a small delay to allow the page time to load

        # Logging in Process
        # Attempts to locate the "Check Access" button, if fail it will timeout and send the following error message
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn > .fontMedium")))
            print("Button found!")
        except TimeoutException:
            print("Button not found within the timeout")
            self.driver.save_screenshot("screenshot.png")  # Save a screenshot for debugging purposes
            raise

        button.click()

        # Institution access - Selects the field and inputs "Tun Hussien Onn Sunway Library"
        self.wait.until(EC.element_to_be_clickable((By.ID, "bdd-email"))).click()
        self.driver.find_element(By.ID, "bdd-email").send_keys("Tun Hussein Onn Sunway Library")

        self.wait.until(EC.element_to_be_clickable((By.ID, "bdd-els-searchBtn"))).click()

        # Waits for the button to be clickable, and subsequently clicks "Tun Hussein Onn Sunway Library"
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tun Hussein Onn Sunway Library')]")))
        element.click()

        # Click on the "Confirm your institution" button
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.ID, "bdd-elsPrimaryBtn3")))
        confirm_button.click()

        # Wait for the target input field to be visible - Student ID and Password fields
        target_element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "login-username-c4f85c18-7dda-4add-abc1-32e4409e1882")))

        # Inputs the Student ID into the Student ID field
        target_element.click()
        target_element.send_keys(student_id)

        # Inputs the Password into the Password field
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-password-c4f85c18-7dda-4add-abc1-32e4409e1882"))).click()
        self.driver.find_element(By.ID, "login-password-c4f85c18-7dda-4add-abc1-32e4409e1882").send_keys(password)

        # Waits for "Sign in" and clicks it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))).click()

        # Waits for the search bar to be visible and loaded - and insert the relevant search query
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".keyword-wrapper .styleguide-input-module__SOgqZ"))).click()
        self.driver.find_element(By.CSS_SELECTOR, ".keyword-wrapper .styleguide-input-module__SOgqZ").send_keys(query)

        # Selects "add date range" to allow for year filtering
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-year-range-button > .Typography-module__lVnit"))).click()

        # Wait for the dropdown to be clickable (Start year) and selects the start year
        dropdown_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Published from')]/select")))
        dropdown_from.find_element(By.XPATH, f".//option[. = '{startyear}']").click()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".DocumentSearchForm-module__u1zT3:nth-child(2) .Select-module__vDMww"))).click()

        # Wait for the dropdown to be clickable (End Year) and selects the end year
        dropdown_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'To')]/select")))
        dropdown_to.find_element(By.XPATH, f".//option[. = '{endyear}']").click()

        # Waits for the "Search" button and presses it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Stack-module__tT3r4 > .Button-module__R359q > .Typography-module__lVnit"))).click()

        # Exporting Process Begins
        # Selects the checkbox next to "All"
        self.wait.until(EC.element_to_be_clickable((By.ID, "bulkSelectDocument-primary-document-search-results-toolbar"))).click()

        # Waits for the "Export" dropdown and selects it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".export-dropdown .Button-module__nc6_8"))).click()

        # Locates the export dropdown menu and clicks on the CSV button
        element = self.driver.find_element(By.CSS_SELECTOR, ".export-dropdown .Button-module__nc6_8")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # Locates the body element of the webpage and creates a new ActionChains object
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).move_by_offset(0, 0).perform()

        # Waits until the CSV button is clickable and clicks on it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    ".Stack-module___CTfk:nth-child(1) > .Button-module__nc6_8:nth-child(2) > .Typography-module__lVnit"))).click()

        # Waits until the "Select all information" button is clickable and clicks on it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    ".FileTypeModal-module__LkjXv > .Stack-module__tT3r4 > .Button-module__nc6_8 > .Typography-module__lVnit"))).click()

        # Waits until the "Export" button is clickable and clicks on it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Button-module__R359q:nth-child(1)"))).click()

        # Defines a function called `check_progress()` that checks the download progress of the CSV file
        # and handles timeouts
        def check_progress(retry_count=0, max_retries=3):
            try:
                # Waits until the download progress bar appears (bottom right corner)
                progress_element = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.Toastify-module__GEB2t progress')))
                # Executes JavaScript to retrieve the value of the progress bar
                progress_value = self.driver.execute_script('return arguments[0].value;', progress_element)
                # Converts the value to a float
                progress_percentage = float(progress_value)

                # Checks if the progress percentage is at 100%
                if progress_percentage == 100.0:
                    # If yes, wait for 1 minute before ending the script
                    time.sleep(60)
                    # and End the script
                    print('Script ended')
                    return

            except TimeoutException:
                if retry_count < max_retries:
                    print(f"Timeout reached while waiting for file download. Retrying... (Retry {retry_count + 1})")
                    time.sleep(5)  # Wait for a few seconds before retrying
                    check_progress(retry_count + 1, max_retries)
                else:
                    # Handle the timeout condition after maximum retries
                    print("Timeout reached after maximum retries. File download failed.")

        # Call the check_progress() function
        check_progress()

        # Close the webdriver instance
        self.driver.quit()

# Run the test
if __name__ == "__main__":
    unittest.main(argv=sys.argv[:1])
    time.sleep(3)  # Wait for 3 seconds after the test completes to allow file download
