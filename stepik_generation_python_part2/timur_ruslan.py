#! python
# -*- coding: utf-8 -*-

"""Камень, ножницы, бумага.

Тимур и Руслан пытаются разделить фронт работы по курсу
"Python для профессионалов". Для этого они решили сыграть в камень,
ножницы и бумагу. Помогите ребятам бросить честный жребий и определить,
кто будет делать очередной модуль нового курса.
"""

# in: echo "камень" "бумага" | python timur_ruslan.py
# out: Руслан

# Словарь со значениями выпавших фигур и условиями победы
m = {'камень-камень': 'ничья',
     'камень-ножницы': 'Тимур',
     'камень-бумага': 'Руслан',
     'ножницы-ножницы': 'ничья',
     'ножницы-бумага': 'Тимур',
     'ножницы-камень': 'Руслан',
     "бумага-бумага": 'ничья',
     'бумага-камень': 'Тимур',
     'бумага-ножницы': 'Руслан'}
timur, ruslan = input(), input()
key = timur + '-' + ruslan
if timur + '-' + ruslan in m:
    # print('Ok')
    print(m[key])
