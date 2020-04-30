#! python
# -*- coding: utf-8 -*-

import datetime as dt


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    if friend in DATABASE:
        if DATABASE[friend] in UTC_OFFSET:
            now = dt.datetime.utcnow()
            period = dt.timedelta(hours=UTC_OFFSET[DATABASE[friend]])
            city_moment = now + period
            return city_moment


print(what_time('Алина'))
