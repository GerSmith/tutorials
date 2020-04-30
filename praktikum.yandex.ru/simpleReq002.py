#! python
# -*- coding: utf-8 -*-

import requests

url = 'http://wttr.in/Kurgan?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа