# для запуска тестов необходимо выполнить в терминале команду:
#python -m pytest -v --driver Chrome --driver-path C:/chrome/chromedriver.exe  test_main_page_catalog.py
from pages.main_page import MainPage
from pages.main_page_catalog import MainPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.elements import ManyWebElements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from tests.data import correct_email,correct_pass
    # incorrect_email,incorrect_pass,correct_product,incorrect_product_title,other_value_for_search
import pytest
import random
# driver=webdriver.Chrome()


# КАТАЛОООООООООООООГ

# def test_power_tools(web_browser):
#     """при клике на ссылку "Электроинструменты"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.power_tools.click()
#     assert page.get_relative_link()=='/catalog/2-0/'and'Электроинструменты' in page.get_page_source(), 'ссылка "Электроинструменты" не ведет на соответствующую страницу'
#
#
# def test_garden_and_cottage(web_browser):
#     """при клике на ссылку "сад и дача"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.garden_and_cottage.click()
#     assert page.get_relative_link()=='/catalog/1003-0/'and'Товары для сада и дачи' in page.get_page_source(), 'ссылка "сад и дача" не ведет на соответствующую страницу'
#
#
#
# def test_welding_equipment(web_browser):
#     """при клике на ссылку "сварочное оборудование"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.welding_equipment.click()
#     assert page.get_relative_link()=='/catalog/5049-0/'and'Сварочное оборудование' in page.get_page_source(), 'ссылка "сварочное оборудование" не ведет на соответствующую страницу'
#
#
# def test_power_equipment(web_browser):
#     """при клике на ссылку "силовая техника"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.power_equipment.click()
#     assert page.get_relative_link()=='/catalog/5-0/'and'Силовая техника' in page.get_page_source(), 'ссылка "силовая техника" не ведет на соответствующую страницу'
#
# def test_hand_tools(web_browser):
#     """при клике на ссылку "ручные инструменты"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.hand_tools.click()
#     assert page.get_relative_link()=='/catalog/5001-0/'and'Ручные инструменты и приспособления' in page.get_page_source(), 'ссылка "ручные инструменты" не ведет на соответствующую страницу'
#
#
# def test_measuring_tool(web_browser):
#     """при клике на ссылку "Измерительные инструмент"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.measuring_tool.click()
#     assert page.get_relative_link()=='/catalog/4-0/'and'Измерительные инструменты' in page.get_page_source(), 'ссылка "Измерительные инструмент" не ведет на соответствующую страницу'
#
# def test_pneumatic_tool(web_browser):
#     """при клике на ссылку "пневматический инструмент"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.pneumatic_tool.click()
#     assert page.get_relative_link()=='/catalog/11-0/'and'Пневматические инструменты' in page.get_page_source(), 'ссылка "пневматический инструмент" не ведет на соответствующую страницу'
#
# def test_machines(web_browser):
#     """при клике на ссылку "станки"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.machines.click()
#     assert page.get_relative_link()=='/catalog/9-0/'and'Станки' in page.get_page_source(), 'ссылка "станки" не ведет на соответствующую страницу'
#
# def test_consumables(web_browser):
#     """при клике на ссылку "расходные материалы"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.consumables.click()
#     assert page.get_relative_link()=='/catalog/6-0/'and'Расходные материалы и оснастка' in page.get_page_source(), 'ссылка "расходные материалы" не ведет на соответствующую страницу'
#
#
# def test_everything_for_construction(web_browser):
#     """при клике на ссылку "все для строительства"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.everything_for_construction.click()
#     assert page.get_relative_link()=='/catalog/5028-0/'and'Всё для строительства' in page.get_page_source(), 'ссылка "все для строительства" не ведет на соответствующую страницу'
#
# def test_climate_heating(web_browser):
#     """при клике на ссылку "климат,отопление и вентиляция"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.climate_heating.click()
#     assert page.get_relative_link()=='/catalog/10-0/'and'Климатическое оборудование' in page.get_page_source(), 'ссылка "климат,отопление и вентиляция" не ведет на соответствующую страницу'
#
# def test_plumbing(web_browser):
#     """при клике на ссылку "сантехника"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.plumbing.click()
#     assert page.get_relative_link()=='/catalog/21-0/'and'Сантехника' in page.get_page_source(), 'ссылка "сантехника" не ведет на соответствующую страницу'
#
# def test_light_electrics(web_browser):
#     """при клике на ссылку "свет и электрика"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.light_electrics.click()
#     assert page.get_relative_link()=='/catalog/1007-0/'and'Свет и электрика' in page.get_page_source(), 'ссылка "свет и электрика" не ведет на соответствующую страницу'
#
#
# def test_car_service(web_browser):
#     """при клике на ссылку "автосервис"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.car_servise.click()
#     assert page.get_relative_link() == '/catalog/1004-0/' and 'Автотовары' in page.get_page_source(), 'ссылка "автосервис" не ведет на соответствующую страницу'
# #
#
#
# из-за того,что появляется поле с надписью,что этот "Используя наш сайт, вы даете согласие на обработку файлов cookie, пользовательских данных. Вы можете настроить типы отслеживаемых данных.
# следующие три теста падают,но почему мне никак не убрать эту табличку,не могу составить на нее локатор,когда запускаешь тесты,ее будто не видно
def test_cleaning(web_browser):
    """при клике на ссылку "уборка и клининг"  происходит переход на соответствующую страницу"""
    page = MainPage(web_browser)
    element = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Уборка и клининг")]')))
    element.click()
    assert page.get_relative_link() == '/catalog/5015-0/' and 'Товары для уборки и клининга' in page.get_page_source(), 'ссылка "уборка и клининг" не ведет на соответствующую страницу'

# def test_household(web_browser):
#     """при клике на ссылку "товары для дома и досуга"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#
#     element = WebDriverWait(web_browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Товары для дома и досуга")]')))
#     element.click()
#     assert page.get_relative_link() == '/catalog/1234-0/' and 'Товары для дома и досуга' in page.get_page_source(), 'ссылка "товары для дома и досуга" не ведет на соответствующую страницу'
#
#
# def test_hardware_fasteners(web_browser):
#     """при клике на ссылку "метизы и крепеж"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#
#     element = WebDriverWait(web_browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Метизы и крепёж")]')))
#     element.click()
#
#     assert page.get_relative_link() == '/catalog/35-0/' and 'Метизы и крепеж' in page.get_page_source(), 'ссылка "метизы и крепеж" не ведет на соответствующую страницу'