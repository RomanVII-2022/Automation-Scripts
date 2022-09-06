from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


service_object = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get("https://itera-qa.azurewebsites.net/home/automation?")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("John Elder")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("222 333 444")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12345")
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("kirekoo-3412")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

driver.find_element(By.XPATH, "//input[@id='female']").click()

days=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
for day in days:
    if day.get_attribute('id') == "monday" or day.get_attribute('id') == "thursday" or day.get_attribute('id') == "saturday":
        day.click()


country = Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))
country.select_by_visible_text("Greece")

driver.find_element(By.XPATH, "//div[@class='custom-file']").click()


time.sleep(5)
driver.quit()
