from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Users\19198\PycharmProjects\SeleniumTestProject1\drivers\chromedriver.exe")
driver = webdriver.Ie()
driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()
