from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException

class BasePage():
    
    # Инициализации класса с конструктором
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
    
    # функция для открытия страницы
    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, search_method, selector):
        try:
            self.browser.find_element(search_method, selector)
        except (NoSuchElementException, NoSuchAttributeException):
            return False
        return True
    