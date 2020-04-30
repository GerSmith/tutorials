#!python
# -*- coding: utf-8 -*-

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    #'lang': 'ru',  # удалите этот параметр
    'M': '',
}

request_headers = {
    # заполните словарь с заголовками
    'Accept-Language': 'ru'
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)
