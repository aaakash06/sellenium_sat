from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://satreg.collegeboard.org/register/testCenter")  # Replace with your target URL

time.sleep(6)

# Find and click the first button (replace with actual locator)
button_1 = driver.find_element(By.ID, "qc-id-login-button-continue")  # Use appropriate selector
button_1.click()

# Fill out the form fields

# Find the text input by name and type a value
email_input = driver.find_element(By.NAME, "username")
email_input.send_keys("bkakash12345@gmail.com")


# Find a submit button and click it to submit the form
submit_button = driver.find_element(By.ID, "idp-discovery-submit")
submit_button.click()

# Find a checkbox and check it
# checkbox = driver.find_element(By.NAME, "remember")
# if not checkbox.is_selected():
#     checkbox.click()
    
time.sleep(2)
    
# Find the text input by name and type a value
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Akash11$$")


# Find a submit button and click it to submit the form
submit_button = driver.find_element(By.ID, "okta-signin-submit")
submit_button.click()

register_button = driver.find_element(By.NAME, "qc-id-registration-card-4098567244-button-finishregistration")
register_button.click()


register_button = driver.find_element(By.CLASS_NAME, "button-blue")
register_button.click()


terms_element = driver.find_element(By.ID, "qc-id-termsconditions-scrollbox-termsconditions")  # Replace with the actual ID or other locator

# Scroll to the bottom of the element using JavaScript
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", terms_element)

# Wait to ensure the scroll happens (adjust as needed)
time.sleep(2)

# Optionally accept the terms by clicking a checkbox or button after scrolling
accept_button = driver.find_element(By.ID, "terms-acceptance-checkbox")
accept_button.click()

continue_button = driver.find_element(By.ID, "qc-id-selectdatecenter-testlocation-button-next")
continue_button.click()
continue_button = driver.find_element(By.ID, "testdate-continue-button")
continue_button.click()
continue_button = driver.find_element(By.ID, "TestCenterRadio")
continue_button.click()
continue_button = driver.find_element(By.ID, "qc-id-selectdatecenter-testcenter-international-button-search")
continue_button.click()


# qc-id-selectdatecenter-testlocation-button-next
# testdate-continue-button
# TestCenterRadio
# qc-id-selectdatecenter-testcenter-international-button-search


# Wait for the page to load (adjust the time based on your site's load time)
time.sleep(2)



# Optionally close the browser
time.sleep(5)  # Allow some time to observe the final page
# driver.quit()
