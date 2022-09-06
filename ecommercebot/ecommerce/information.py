from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class Information:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def phone_info(self):
        phones = self.driver.find_elements(By.XPATH, "//div[@class='details']")
        all = []
        for phone in phones:
            phone_name = phone.find_element(By.CLASS_NAME, "product-title")
            phone_price = phone.find_element(By.CLASS_NAME, "prices")
            all.append([phone_name.text, phone_price.text])

        table = PrettyTable(['Phone Name', 'Phone Price'])
        table.add_rows(all)
        print(table)