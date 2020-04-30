#! python
# -*- coding: utf-8 -*-

import requests

response = requests.get('https://ya.ru/white')

# вот мы узнали, что код ответа 200 и заполучили это число в свой код:
code = response.status_code
print(f'Код ответа = {code}')

# а вот мы и заголовки читаем, и выводим их форматированной строкой
# с примечанием, каким захочется, на любом языке
headers = response.headers
print(f'Тип содержимого: {headers["content-type"]}')
print(f'Время ответа: {headers["date"]}')

"""
for key, value in headers.items():
    print(f'{key} - {value}')
"""

new_response = requests.get('https://praktikum.yandex.ru/notfound')
print(new_response.status_code)
