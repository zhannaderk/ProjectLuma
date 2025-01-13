class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://magento.softwaretestingboard.com/"

    def open(self):
        """Відкриває домашню сторінку."""
        self.driver.get(self.url)

    def is_title_correct(self):
        """Перевіряє правильність заголовка сторінки."""
        return "Home Page" in self.driver.title
