import pages.home_page


def test_home_page_title(driver):
    # Створюємо об'єкт сторінки
    home_page = pages.home_page.HomePage(driver)

    # Відкриваємо сторінку
    home_page.open()

    # Перевіряємо, чи правильний заголовок
    assert home_page.is_title_correct(), "Home Page title is incorrect"
