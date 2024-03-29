#! python
# -*- coding: utf-8 -*-

"""Скрипт игры шар судьбы.

Магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
Скрипт просит пользователя задать некий вопрос, чтобы случайным образом на него ответить.
"""

import random

magic_dict = {
    'positive': ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом'],
    'doubt': ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да'],
    'neutral': ['Пока неясно, попробуй снова', 'Спроси позже', 'Не стоит', 'Сейчас нельзя предсказать', 'Спроси опять'],
    'negative': ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
                 'Перспективы не очень хорошие', 'Весьма сомнительно']
}


def get_value():
    """Функция возвращает значение-ответ из словаря magic_dict."""
    value = random.choice(list(magic_dict.values()))
    return value[random.randrange(len(value))]


while True:
    if input('Задай мне свой вопрос: ') != '':
        print(get_value())
    else:
        break
