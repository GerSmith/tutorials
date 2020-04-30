#! python
# -*- coding: utf-8 -*-

import requests

#url = 'https://wttr.in' 
url = 'https://wttr.in/Kurgan' 

weather_parameters = {
    #'Kurgan': '',
    '0': '',
    #'1': '',
    #'2': '',
    'T': '',
    'M': '',
    'lang': 'ru'
}

response = requests.get(url, params=weather_parameters)

print(response.status_code)
print(response.url)
print(response.text)
