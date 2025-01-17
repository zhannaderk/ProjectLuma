import sys
import os
import pytest
from pytest_bdd import scenarios, given, then
from conftest import driver
from pages.home_page import HomePage


# Додаємо шлях до каталогу pages
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


scenarios('features/home_page.feature')


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@given('the home page is open')
def open_home_page(home_page):
    home_page.open()


@then('the title should be correct')
def verify_home_page_title(home_page):
    assert home_page.is_title_correct(), "Home Page title is incorrect"
