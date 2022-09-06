from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


service_object = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("performance_glitch_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

filter = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
filter.select_by_visible_text("Price (low to high)")

#inventory = mywait.until(EC.presence_of_element_located(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']"))
action = ActionChains(driver)
onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
bolt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")

action.move_to_element(onesie).click()
action.move_to_element(bolt).click()
action.move_to_element(jacket).click()
action.perform()

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
driver.find_element(By.XPATH, "//button[@id='checkout']").click()


driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("John")
driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Elder")
driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("abd-7812")
driver.find_element(By.XPATH, "//input[@id='continue']").click()


info = driver.find_elements(By.XPATH, "//div[@class='summary_info']/div")
for i in range(len(info)-1):
    print(info[i].text)

driver.find_element(By.XPATH, "//button[@id='finish']").click()


driver.quit()