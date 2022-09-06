from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from ecommerce.constants import BASE_DIR
from selenium.webdriver import ActionChains
from ecommerce.information import Information


class Shopping:
    def __init__(self, driver = webdriver.Chrome(service=Service("C:\Program Files (x86)\chromedriver.exe")), teardown=True):
        self.driver = driver
        self.teardown = teardown
        super(Shopping, self).__init__()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()


    def get_home_page(self):
        self.driver.get(BASE_DIR)


    def phones(self):
        electronics = self.driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
        cell_phones = self.driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']")
        action = ActionChains(self.driver)
        action.move_to_element(electronics)
        action.move_to_element(cell_phones).click().perform()


    def infomation(self):
        info = Information(driver=self.driver)
        info.phone_info()
        
        