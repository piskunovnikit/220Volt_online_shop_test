# для запуска тестов необходимо выполнить в терминале команду:
#python -m pytest -v --driver Chrome --driver-path C:/chrome/chromedriver.exe  test_auth_page.py
from pages.auth_page import AuthPage
from pages.main_page import MainPage
import time
import pytest
import random
from tests.data import correct_email,correct_pass,incorrect_email,incorrect_pass,correct_product,incorrect_product_title,other_value_for_search



def test_authorisation_with_correct_data(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    time.sleep(1)
    assert page.get_relative_link() == '/catalog/','При вводе в поля формы авторизации корректных данных действующего пользователя не происходит вход в аккаунт'

@pytest.mark.parametrize("email",list(incorrect_email.keys())[:],
                         ids=list(incorrect_email.values())[:])
def test_auth_with_empty_email(web_browser,email):
    """при вводе в поле для email возможные неверные варианты значений сообщение об с сообщением об ошибке"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    # time.sleep(1) Пароль: Это поле не может быть пустым.
    assert page.incorrect_email_message.is_visible() ,"сообщение об ошибке не появилось,вход успешный"



@pytest.mark.parametrize("passw",list(incorrect_pass.keys())[0:8],
                         ids=list(incorrect_pass.values())[0:8])
def test_auth_with_empty_pass(web_browser,passw):
    """при вводе в поле для пароля возможные неверные варианты значений появляется сообщение об ошибке"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(passw)
    page.login_button.click()
    assert page.incorrect_email_message.is_visible() ,"сообщение об ошибке не появилось,вход успешный"








