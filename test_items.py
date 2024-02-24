import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver

links = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
    'http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/'
]

@pytest.mark.parametrize('link', links)
def test_find_add_to_basket_button(browser, link):
    browser.get(link)
    time.sleep(30)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    br_language = browser.find_element(By.CSS_SELECTOR, "html[lang]")
    br_lang = br_language.text
    assert br_lang != curr_language, \
        f"Ожидаемый язык {curr_language} не совпадает с фактическим {br_lang}"
    find_buttons = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form .btn")
    assert len(find_buttons) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(find_buttons) < 2, 'Кнопка добавления в корзину не уникальна'
