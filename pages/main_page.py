from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    
    # функция для перехода по ссылке на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 
    
    # для проверки наличия ссылки для логина
    def check_login_link(self):
        assert self.is_element_present.find_element(By.CSS_SELECTOR, "#invalid_login_link"), "The element is not present"
    