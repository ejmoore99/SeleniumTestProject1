from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to the ChromeDriver executable
chrome_driver_path = '../drivers/chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Set implicit wait time
driver.implicitly_wait(10)

# Maximize the browser window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Locate the search box using its name attribute and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("What is the purpose of Selenium WebDriver?")

# Locate the search button using its name attribute and click it
search_button = driver.find_element(By.NAME, "btnK")
search_button.send_keys(Keys.RETURN)  # Use Keys.RETURN to simulate pressing Enter

# Wait for some time to view the search results
time.sleep(10)  # Wait for 10 seconds

# Close the browser
driver.close()
driver.quit()

print("Test Completed")