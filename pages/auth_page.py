from pages.base_page import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.220-volt.ru/login/'
        super().__init__(web_driver, url)


    email_field = WebElement(xpath='//input[@name="user_email"]')
    pass_field = WebElement(xpath='//input[@id="user_password"]')
    login_button = WebElement(xpath='//*[@id="link_login"]')
    forget_pass = WebElement(xpath='//a[@id="forget"]')
    reg_button = WebElement(xpath='//a[@id="reg"]')
    profile_button = WebElement(xpath='//a[@span="вход"]')
    incorrect_email_message = WebElement(xpath='//div[@class="login_error phbspace-10 text-red"]')
    power_tools = WebElement(xpath='//span[contains(text(),"Электроинструменты")]')