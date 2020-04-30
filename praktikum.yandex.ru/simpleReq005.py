#! python
# -*- coding: utf-8 -*-

import requests

request_headers = {
    #'Accept-Language': 'ru'  # попросим материал на русском языке
    'Accept-Language': 'en'  # попросим материал на русском языке
}

# сходим почитать блоги про IT, строкой передаём URL платформы habr
response = requests.get('https://habr.com', headers=request_headers)

print(response.text[:305])
