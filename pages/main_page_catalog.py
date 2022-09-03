import os,pickle

from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
import json
from urllib.parse import urlparse

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.220-volt.ru/'

        super().__init__(web_driver, url)

        # with open('cookies.tmp', 'rb') as cookiesfile:
        #     cookies = pickle.load(cookiesfile)
        # for cookie in cookies:
        #     web_driver.add_cookie(cookie)
        # web_driver.refresh()

    power_tools = WebElement(xpath='//span[contains(text(),"Электроинструменты")]')
    garden_and_cottage = WebElement(xpath='//a[@title="Сад и дача"]')
    welding_equipment = WebElement(xpath='//span[contains(text(),"Сварочное оборудование")]')
    power_equipment = WebElement(xpath='//span[contains(text(),"Силовая техника")]')
    hand_tools = WebElement(xpath='//a[@title="Ручные инструменты"]')
    measuring_tool = WebElement(xpath='//a[@title="Измерительный инструмент"]')
    pneumatic_tool = WebElement(xpath='//span[contains(text(),"Пневматический инструмент")]')
    machines = WebElement(xpath='//a[@title="Станки"]')
    consumables = WebElement(xpath='//span[contains(text(),"Расходные материалы")]')
    everything_for_construction = WebElement(xpath='//span[contains(text(),"Всё для строительства")]')
    climate_heating = WebElement(xpath='//span[contains(text(),"Климат, Отопление и Вентиляция")]')
    plumbing = WebElement(xpath='//span[contains(text(),"Сантехника")]')
    light_electrics = WebElement(xpath='//a[@title="Свет и электрика"]')
    car_service = WebElement(xpath='//a[@title="Автосервис"]')
    cleaning = WebElement(xpath='//span[contains(text(),"Уборка и клининг")]')
    household = WebElement(xpath='//span[contains(text(),"Товары для дома и досуга")]')
    hardware_fasteners = WebElement(xpath='//span[contains(text(),"Метизы и крепёж")]')
    close_button = WebElement(xpath='//main[@class="widget"]')
    sort_products_by_price = WebElement(css_selector='button[data-fl-close=""]')

