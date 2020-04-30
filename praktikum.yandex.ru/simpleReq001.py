#! python
# -*- coding: utf-8 -*-

import requests

response = requests.get('https://ya.ru/white')

print(response.text)