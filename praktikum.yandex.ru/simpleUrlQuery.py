#!python
# -*- coding: utf-8 -*-

import urllib.parse
"""
user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' + '%20'.join(user_query.split()) # ваш код здесь

print(url)


strings = [
    'что такое backend',
    'Привет!',
    ' ',  # просто пробел
    'letiště',  # аэропорт по-чешски
    'München',  # крупнейший город Баварии
    'Champs-Élysées',  # Елисейские поля
    '東京',  # а это Токио, столица Японии  :)
]

for s in strings:
    encoded = urllib.parse.quote(s)  # зашифрованная строка
    decoded = urllib.parse.unquote(encoded)  # расшифрованная обратно строка
    print(decoded, '-', encoded)
"""

url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

to_encode = url.split('=')[-1]
print(urllib.parse.unquote(to_encode))
