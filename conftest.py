import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Фікстура для створення драйвера Selenium для Chrome з параметрами:
    - headless режим (без графічного інтерфейсу)
    - шлях до ChromeDriver
    Після завершення тесту драйвер закривається.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    service = Service('../../../../CyberBionic_Test/chrome-win64/chrome-win64/chrome.exe')  # Вкажіть правильний шлях до chromedriver.exe
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()