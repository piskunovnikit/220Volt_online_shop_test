import random
import string

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def generate_string(n):
    return n*'x'

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

correct_email = "lomnik1995@yandex.ru"
correct_pass = "qazwsxedc"

incorrect_email={'':'empty string',
                 ' ':'whitespace',
                 'pilip.ford@yandex.ru':'uncorrect email',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}
incorrect_pass={'':'empty string',
                 ' ':'whitespace',
                 '1qaz2wsx3edc':'uncorrect pass',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}

correct_product=['степлер','лобзик','перфоратор','дрель',]
incorrect_product_title={
'лобзик':'first capital letter',
    'ЛоБзИк':'fence',
    'ЛОБЗИК':'all lower case',
    ' лобзик':'space at the beginning',
    'лоб зик':'space in the middle',
    'лобзик ':'space at the end',
    'лозик':'missing letter',
    'лопзик':'spelling mistake',
    'лобзик)))':'special characters at the end',
    ')))лобзик':'space at the beginning',
    'лоб.зик':'space in the middle',
    ',kj,pbr':'English layout',
    'lobzik':'Latin alphabet'
}
other_value_for_search={
                 generate_random_string(10): 'non-existent product',
                 generate_string(255):'255 symbols',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123456789':'digit'
}