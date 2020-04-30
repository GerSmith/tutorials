#! python
# -*- coding: utf-8 -*-

import datetime as dt


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


def what_time(city):
    # напишите код тела функции
    # пусть она вернет время в городе city
    if city in UTC_OFFSET:
        #return f'we have {city} in dict'
        now = dt.datetime.utcnow()
        period = dt.timedelta(hours=UTC_OFFSET[city])
        city_moment = now + period
        return city_moment
    else:
        return f'we haven\'t {city} in dict'


print(what_time('Екатеринбург'))
print(what_time('Курган'))