# для запуска тестов необходимо выполнить в терминале команду:
#python -m pytest -v --driver Chrome --driver-path C:/chrome/chromedriver.exe  test_main_page.py

from pages.main_page import MainPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.elements import ManyWebElements
from data import correct_product, incorrect_product_title,other_value_for_search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from tests.data import correct_email,correct_pass
    # incorrect_email,incorrect_pass,correct_product,incorrect_product_title,other_value_for_search
import pytest
import random
# driver=webdriver.Chrome()


# def test_change_cities(web_browser):
#     """при клике на ссылку города"Санкт-Петербург у меня" открывается окно с городами"""
#     page = MainPage(web_browser)
#     page.change_cities.click()
#     time.sleep(1)
#     res = page.panel_sities.wait_until_not_visible()
#
#     assert res, 'Кнопка "город Санкт-Петербург" не вызывает выпадающее меню'
#
# def test_order_status(web_browser):
#     """при клике на ссылку "статус заказа" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.order_status.click()
#     assert page.get_relative_link()=='/order-status/','Ссылка "статус заказа" не ведет на соответствующую страницу'
#
#
# def test_shops(web_browser):
#     """при клике на ссылку "магазины" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.shops.click()
#     assert page.get_relative_link()=='/shop/1/city-7800000000000/','Ссылка "магазины" не ведет на соответствующую страницу'
#
# def test_delivery(web_browser):
#     """при клике на ссылку "оплата и доставка" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.delivery.click()
#     assert page.get_relative_link()=='/delivery/','Ссылка "оплата и доставка" не ведет на соответствующую страницу'
#
# def test_legal_entities (web_browser):
#     """при клике на ссылку "юрдицам" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.legal_entities.click()
#     assert page.get_relative_link()=='/info/wholesale/','Ссылка "юрлицам" не ведет на соответствующую страницу'
#

# def test_franchising(web_browser):
#     """при клике на ссылку "франчайзинг" на главной страницы сайта происходит переход на происходит переход на соответствующую страницу """
#     page = MainPage(web_browser)
#
#     # web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     page.franchising.click()
#     # time.sleep(1)
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url=='https://franchise.220-volt.ru/?utm_source=220_volt&utm_medium=referral',"Ссылка 'юрлицам' не ведет на соответствующую страницу"
#
# def test_main_logo (web_browser):
#     """при клике на главный логотип "220 ВОЛЬТ происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.main_logo.click()
#     assert page.get_current_url()=='https://www.220-volt.ru/','Ссылка "220 ВОЛЬТ" не ведет на соответствующую страницу'
#
# # def test_bonus (web_browser):
#     """при клике на ссылку "бонусы" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.bonus.click()
#     assert page.get_relative_link()=='/club-220/','Ссылка "бонусы" не ведет на соответствующую страницу'
#
# def test_catalog (web_browser):
#     """при клике на ссылку "каталог" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.catalog.click()
#     assert page.get_relative_link()=='/catalog/','Ссылка "каталог" не ведет на соответствующую страницу'
#
# def test_user_icon (web_browser):
#     """при клике на иконку профиля  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.user_icon.click()
#     assert page.get_relative_link()=='/login/','кнопка иконка профиля не ведет на соответствующую страницу'
# # разобраться с куками в тесте сверху
#
# def test_favorites(web_browser):
#     """при клике на иконку "избранное" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.favorites_icon.click()
#     assert page.get_relative_link()=='/profile/favorites/','иконка "избранное" не ведет на соответствующую страницу'
#
# def test_cart(web_browser):
#     """при клике на ссылку "избранное" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.favorites_icon.click()
#     assert page.get_relative_link()=='/profile/favorites/','Ссылка "избранное" не ведет на соответствующую страницу'
# #     разобраться с куками
#
# def test_promo(web_browser):
#     """при клике на ссылку "промокод" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.promo.click()
#     assert page.get_relative_link()=='/promo/promokod_stm/','Ссылка "промокод" не ведет на соответствующую страницу'
#
# def test_discount(web_browser):
#     """при клике на ссылку "скидки" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.discount.click()
#     assert page.get_relative_link()=='/share/0/','Ссылка "скидки" не ведет на соответствующую страницу'
#
# def test_discount_legal_entities(web_browser):
#     """при клике на ссылку "скидки юр.лицам" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.discount_legal_entities.click()
#     assert page.get_relative_link()=='/info/wholesale/','Ссылка "скидки юр.лицам" не ведет на соответствующую страницу'
#
# def test_hammer_brand(web_browser):
#     """при клике на ссылку "hammer" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.hammer_brand.click()
#     assert page.get_relative_link()=='/promo/hammer_brand/','ссылка "hammer" не ведет на соответствующую страницу'
#
# #
# def test_circular_saw(web_browser):
#     """при клике на ссылку "циркулярные пилы" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.circular_saw.click()
#     assert page.get_relative_link()=='/catalog/pily-cirkuljarnye/','ссылка "циркулярные пилы" не ведет на соответствующую страницу'
#
# def test_bulgarian_saw(web_browser):
#     """при клике на ссылку "болгарки" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.bulgarian_saw.click()
#     assert page.get_relative_link()=='/catalog/bolgarki-ushm/','ссылка "болгарки" не ведет на соответствующую страницу'
#
#
# def test_petrol_trimmers(web_browser):
#     """при клике на ссылку "бензиновые триммеры" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.petrol_trimmers.click()
#     assert page.get_relative_link()=='/catalog/motokosi/','ссылка "бензиновые тримееры" не ведет на соответствующую страницу'
#
# def test_lawn_mowers(web_browser):
#     """при клике на ссылку "газонокосилки" происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.lawn_mowers.click()
#     assert page.get_relative_link()=='/catalog/gazonokosilki/','ссылка "газонокосилки" не ведет на соответствующую страницу'
#
# def test_discount_center(web_browser):
#     """при клике на ссылку "дисконт-центр"  происходит переход на соответствующую страницу"""
#     page = MainPage(web_browser)
#     page.discount_Center.click()
#     assert page.get_relative_link()=='/discount/','ссылка "дисконт-центр" не ведет на соответствующую страницу'
#



# низ сайта




# def test_vkontakte(web_browser):
#     """при клике на иконку "вконтакте" на главной страницы сайта происходит переход на происходит переход на соответствующую страницу """
#     page = MainPage(web_browser)
#     page.vk_ikon.click()
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url=='https://vk.com/likevolt',"иконка 'вконтакте' не ведет на соответствующую страницу"
#
# def test_youtube(web_browser):
#     """при клике на иконку "youtube" на главной страницы сайта происходит переход на происходит переход на соответствующую страницу """
#     page = MainPage(web_browser)
#     page.youtube_ikon.click()
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url=='https://www.youtube.com/user/220volt220',"иконка 'youtube' не ведет на соответствующую страницу"
#
#
# def test_whatsapp(web_browser):
#     """при клике на иконку "whatsapp" на главной страницы сайта происходит переход на происходит переход на соответствующую страницу """
#     page = MainPage(web_browser)
#     page.whatsapp_ikon.click()
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url=='https://api.whatsapp.com/message/AYXR4E7LUBRQH1?autoload=1&app_absent=0',"иконка 'whatsapp' не ведет на соответствующую страницу"

# def test_telegram(web_browser):
#     """при клике на иконку "whatsapp" на главной страницы сайта происходит переход на происходит переход на соответствующую страницу """
#     page = MainPage(web_browser)
#     page.telegram_ikon.click()
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url=='https://t.me/likevolt_bot',"иконка 'telegram' не ведет на соответствующую страницу"

# def test_yandex_market(web_browser):
#     # тест иногда падает,когда всплывающее окно загораживает кнопку перехода на яндекс маркет,окно никак не сбросить
#     page = MainPage(web_browser)
#     html = web_browser.find_element(By.TAG_NAME, 'html')
#     html.send_keys(Keys.END)
#     element = WebDriverWait(web_browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//a[@href="https://market.yandex.ru/shop/39581/reviews/add"]')))
#     element.click()
#     web_browser.switch_to.window(web_browser.window_handles[1])
#     assert web_browser.current_url == 'https://market.yandex.ru/shop/39581/reviews/add' and 'Отзыв о магазине «220 Вольт»' in page.get_page_source(), "ссылка 'яндекс-маркет' не ведет на соответствующую страницу"





# def test_added_in_carrt(web_browser):
#     """при нажатии на кнопку "Купить" на карточке товара счетчик корзины увеличивается на 1"""
#     page = MainPage(web_browser)
#
#     WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[(@data-product-category-id="288" and @data-product-title="Перфоратор WERT ERH 0724HRE" and @data-product-warranty="12")]'))).click()
#     count = int(page.ikon_quantity.get_text())
#     page.add_in_cart.click()
#     page.continue_shopping.click()
#     countnew = int(WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.ID, 'bQuantity'))).text)
#     assert countnew ==(count+1), 'при нажатии на кнопку "Купить" на карточке товара счетчик корзины не увеличивается на 1'



# def test_auth_with_correct_data(web_browser):
#     """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
#
#     page = MainPage(web_browser)
#     hap =(WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="header-panel-text text-center"]'))).text)
#     page.user_icon.click()
#
#     page.email_field.send_keys(correct_email)
#     page.pass_field.send_keys(correct_pass)
#     page.login_button.click()
#     time.sleep(2)
#     res = (WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="header-panel-text text-center"]'))).text)
#
#     assert "Вход" not in res, 'При вводе в поля формы авторизации корректных данных действующего пользователя не происходит вход в аккаунт'


# def test_sort_product_by_price_from_min(web_browser):
#     """при нажатии кнопки сортировки товаров по критерию "сначала подешевле" товары сортируются от самых дешевых к самым дорогим"""
#     page = MainPage(web_browser)
#     page.power_tools.click()
#     time.sleep(1)
#     page.chainsaws.click()
#     select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@class="listing-select listing-select-sort select2-hidden-accessible"]')))
#     select_object_sort = Select(select_element_sort)
#     time.sleep(1)
#     select_object_sort.select_by_index('1')
#     all_prices=ManyWebElements(xpath='//ins[contains(text(),"")]').get_text()
#     all_prices=[float(pr.replace(' ','')) for pr in all_prices]
#     assert all_prices==sorted(all_prices)

# def test_sort_product_by_price_from_min(web_browser):
#     """при нажатии кнопки сортировки товаров по критерию "сначала подешевле" товары сортируются от самых дешевых к самым дорогим"""
#     page = MainPage(web_browser)
#
#     page.search_field.click()
#     page.search_field.send_keys('телевизор')
#     page.search_button.click()
#     select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="js__listingSort_ID"]')))
#     select_object_sort = Select(select_element_sort)
#     select_object_sort.select_by_value('price-asc')
#     all_prices=ManyWebElements(xpath='//span[@class="price regular"]').get_text()
#     all_prices=[float(pr.replace(' ','')) for pr in all_prices]
#     assert all_prices!=sorted(all_prices)


def test_search_field(web_browser):
     """в результате поиска через поисковую строку главной страницы отображаются товары с названием, соответствующим введенному в строку тексту"""
     page = MainPage(web_browser)
     page.search_field.click()
     product=random.choice(correct_product)
     page.search_field.send_keys("дрель")
     page.search_field.send_keys(Keys.ENTER)
     page.wait_page_loaded()
     page.scroll_down(250)
     # page.products_titles.get_text()
     # for title in page.products_titles.get_text():
     #     # print(title)
     #     assert product in title.lower(), f'Поиск через поисковую строку выдал товар с названием, не соответствующим введенному тексту - {title}'

# @pytest.mark.parametrize("product",list(incorrect_product_title.keys()),
#                          ids=list(incorrect_product_title.values()))
# def test_search_field_incorrect(web_browser,product):
#      """при вводе в поисковую строку главной страницы названия товара с орфографическими ошибками, пробелами, в различном регистре, латиницей,
#     в английской раскладке в результате поиска отображаются товары с названием, соответствующим введенному в строку тексту"""
#      page = MainPage(web_browser)
#      page.search_field.click()
#      page.search_field.send_keys(product)
#      page.search_field.send_keys(Keys.ENTER)
#      page.scroll_down(250)
#      page.products_titles.get_text()
#      for title in page.products_titles.get_text():
#          assert product in title.lower(), f'Поиск через поисковую строку выдал товар с названием, не соответствующим введенному тексту - {title}'
#
#
#
# @pytest.mark.parametrize("value",list(other_value_for_search.keys()),
#                          ids=list(other_value_for_search.values()))
# # @pytest.mark.xfail
# def test_other_value_for_search_field(web_browser,value):
#     """при вводе в поисковую строку главной страницы спецсимволов, китайских символов, очень длинной строки или цифр
#     появляется сообщение о том, что введенное значение некорректно
#     тест помечен как падающий, поскольку при вводе произвольного набора букв появляется сообщение о том, что товары не найдены,
#     при вводе спецсимволов происходит переход на недоступную страницу (сайт не может обработать этот запрос),
#     при вводе китайских символов или очень длинной строки происходит переход на пустую страницу"""
#     page = MainPage(web_browser)
#     page.search_field.click()
#     page.search_field.send_keys(value)
#     page.search_field.send_keys(Keys.ENTER)
#     assert 'Ваш запрос "" не дал результатов.Попробуйте поискать товар вручную, перейдя в полный каталог.' in page.get_page_source(),'При вводе в поисковую строку главной страницы спецсимволов,' \
#                                                           ' китайских символов, очень длинной строки или цифр\
#                                                          в результате поиска не отображается сообщение о том, что введенное значение некорректно'
    # python -m pytest -v --driver Chrome --driver-path C:/chrome/chromedriver.exe  test_main_page.py