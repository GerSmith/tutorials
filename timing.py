#!python
# -*- coding: utf-8 -*-

"""Скрипт работы с функциями времени.

Правильное измерение времени выполнения скрипта осуществляется через функцию
monotonic() модуля time, функция time() зависит от временной зоны.
"""

import time

start_time = time.time()

time.sleep(10)

print(f'Прошло {time.time() - start_time} секунд')

start_time = time.monotonic()

time.sleep(10)

print(f'Прошло {time.monotonic() - start_time} секунд')
