from calendar import month
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

service_object = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("django")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

results = mywait.until(EC.presence_of_all_elements_located((By.ID, "wikipedia-search-result-link")))
for result in results:
   if result.text == "Django (web framework)":
    result.click()

driver.switch_to.window(driver.current_window_handle)

driver.find_element(By.XPATH, "//button[normalize-space()='Click Me']").click()
popup=driver.switch_to.alert
popup.accept()

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

month = "September"
year = "2022"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']")
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    
    if mon.text == month and yr.text == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == "24":
        date.click()

speed = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
speed.select_by_visible_text("Fast") 

file = Select(driver.find_element(By.XPATH, "//select[@id='files']"))
file.select_by_visible_text("DOC file")

number = Select(driver.find_element(By.XPATH, "//select[@id='number']"))
number.select_by_visible_text("5")

product = Select(driver.find_element(By.XPATH, "//select[@id='products']"))
product.select_by_visible_text("Yahoo")

animal = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
animal.select_by_visible_text("Avatar")

labels = driver.find_elements(By.XPATH, "//div[@id='Text1']//div[@class='widget-content']//span")
for i in range(3,6):
    print(labels[i].text)

print("=======================")
employees = driver.find_elements(By.XPATH, "//div[@id='HTML14']//div[@class='widget-content']//employee")
for employee in employees:
    if employee.get_attribute("id") == "2":
        print(employee.text)


signup = driver.find_element(By.XPATH, "//iframe[@id='frame-one1434677811']")
driver.switch_to.frame(signup)
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-1']").send_keys("John")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-2']").send_keys("Elder")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-3']").send_keys("111 222 333")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-4']").send_keys("Sweden")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-5']").send_keys("Tokyo")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-6']").send_keys("abc@gmail.com")

time_of_day=Select(driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-9']"))
time_of_day.select_by_visible_text("Afternoon")
driver.switch_to.default_content()

    
field = driver.find_element(By.XPATH, "//input[@id='field1']")
field.clear()
field.send_keys("Selenium")

d_click = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
action = ActionChains(driver)
action.double_click(d_click)
action.perform()

source = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.XPATH, "//div[@id='droppable']")
action.drag_and_drop(source, target).perform()

source2 =driver.find_element(By.XPATH, "//li[2]")
target2 = driver.find_element(By.XPATH, "//div[@id='trash']")
action.drag_and_drop(source2, target2).perform()

filt = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
action.drag_and_drop_by_offset(filt, 50, 0).perform()

resize = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
action.drag_and_drop_by_offset(resize, 5, 7).perform()


rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr") 
no_rows = len(rows)
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
no_columns = len(columns)

for c in range(1, no_columns+1):
    header = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[1]/th["+str(c)+"]")
    print(header.text, end="               ")
print()

for r in range(2, no_rows+1):
    for c in range(1, no_columns+1):
        tabledata = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]")
        print(tabledata.text, end="             ")
    print()

for r in range(2, no_rows+1):
    subject = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[3]")
    if subject.text == "Selenium":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]")
        print(bookname.text)
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]")
        print(price.text)


tooltips = driver.find_element(By.XPATH, "//a[normalize-space()='Tooltips']")
action.move_to_element(tooltips).perform()
time.sleep(3)

themeroller = driver.find_element(By.XPATH, "//a[normalize-space()='ThemeRoller']")
action.move_to_element(themeroller).perform()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='age']").send_keys("Too old to know better")






time.sleep(5)
driver.quit()