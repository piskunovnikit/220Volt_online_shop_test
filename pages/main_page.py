import os,pickle

from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.auth_page import AuthPage
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

    change_cities=WebElement(xpath='//a[@href="/cities/"]')
    panel_sities=WebElement(id='city-list-modal')
    order_status=WebElement(xpath='//a[@href="https://www.220-volt.ru/order-status/"]')
    shops=WebElement(xpath='//a[@href="/shop/"]')
    delivery=WebElement(xpath='//a[@href="/delivery/"]')
    legal_entities=WebElement(xpath='//a[@href="/info/wholesale/"]')
    franchising=WebElement(xpath='//a[@href="https://franchise.220-volt.ru/?utm_source=220_volt&utm_medium=referral"]')
    main_logo=WebElement(xpath='//img[@alt="220 Вольт"]')
    bonus=WebElement(xpath='//a[@href="/club-220/"]')
    discounts=WebElement(xpath='//span[@class="menu-catalog-item-text"]')
    catalog=WebElement(xpath='//span[contains(text(),"Каталог")]')
    user_icon = WebElement(xpath='//span[@class="header-panel-text text-center"]')
    favorites_icon = WebElement(xpath='//i[@class="header-panel-fav-icon"]')
    cart = WebElement(xpath='//i[@class="header - panel - cart - icon"]')
    promo = WebElement(xpath='//a[@href="/promo/promokod_stm/"]')
    discount = WebElement(xpath='//a[@title="Скидки"]')
    discount_legal_entities = WebElement(xpath='//a[@href="https://www.220-volt.ru/info/wholesale/"]')
    hammer_brand = WebElement(xpath='//a[@title="Hammer"]')
    circular_saw = WebElement(xpath='//a[@title="Циркулярные пилы"]')
    bulgarian_saw = WebElement(xpath='//a[@title="Болгарки"]')
    petrol_trimmers = WebElement(xpath='//a[@title="Бензиновые триммеры"]')
    lawn_mowers = WebElement(xpath='//a[@href="/catalog/gazonokosilki/"]')
    discount_Center = WebElement(xpath='//a[@title="Дисконт-центр"]')
    vk_ikon = WebElement(xpath='//a[@href="https://vk.com/likevolt"]')
    youtube_ikon = WebElement(xpath='//a[@href="https://www.youtube.com/user/220volt220"]')
    whatsapp_ikon = WebElement(xpath='//a[@href="https://wa.me/message/AYXR4E7LUBRQH1"]')
    telegram_ikon = WebElement(xpath='//a[@href="https://t.me/likevolt_bot"]')
    yandex_market= WebElement(xpath='//a[@href="https://market.yandex.ru/shop/39581/reviews/add"]')
    added_in_cart=WebElement(xpath='//a[(@data-product-category-id="288" and @data-product-title="Перфоратор WERT ERH 0724HRE" and @data-product-warranty="12")]')
    # added_in_cart=WebElement(xpath='//a[contains(@data-product-category-id, "288" and @data-product-variant="1")]')
    continue_shopping=WebElement(xpath='//a[(@class="btn-light-yellow-flat box-inline btn text-center text-underline-none radius-6 mvrspace-20")]')
    add_in_cart =WebElement(xpath='//a[(@class=" ecommerce-tracked-product in-cart box-inline mspace-0 phspace-10 pvspace-15 bg-yellow-gradient divider-yellow text-underline-none box-model-border radius-3 delivery-date-ok ecommerce-tracked-detail text-strong text-center text-h4 col-12 ")]'  )
    ikon_quantity=WebElement(id='bQuantity')
    email_field = WebElement(xpath='//input[@name="user_email"]')
    pass_field = WebElement(xpath='//input[@id="user_password"]')
    login_button = WebElement(xpath='//*[@id="link_login"]')
    chainsaws = WebElement(xpath='//img[@alt="Бензопилы"]')
    select_sort =WebElement(xpath='//select[@class="listing-select listing-select-sort select2-hidden-accessible"]')
    prise_small_to_big = WebElement(id='select2-o76g-container')
    power_tools = WebElement(xpath='//span[contains(text(),"Электроинструменты")]')
    search_field=WebElement(xpath='//input[@type="search"]')
    products_titles=ManyWebElements(xpath='//div[@class="retailrocket-item-title"]')
    # products_titles=ManyWebElements(xpath='//span[contains(text(),"Перфоратор HAMMER PRT620D")]')
    product_kategory = ManyWebElements(xpath='//a[@class="sCM__item__link"]')


































