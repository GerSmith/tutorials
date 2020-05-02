#!python
# -*- coding: utf-8 -*-

# 10 практик кода, ускоряющих выполнение программ на Python
import random
import time

# I. Используй стандартные функции
random.seed(666)

a_long_list = [random.randint(0, 50) for i in range(1000000)]

a_dict = {'A': 1, 'B': 3, 'C': 2, 'D': 4, 'E': 5}

another_long_list = [random.randint(0,500) for i in range(1000000)]

# 1. Кастомная реализация set
print('Кастомная реализация set')
start_time = time.monotonic()               # запускаем отсчёт времени

unique = []
for n in a_long_list:
    if n not in unique:
        unique.append(n)

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# 2. Встроенная функция set
print('Встроенная функция set')
start_time = time.monotonic()               # запускаем отсчёт времени

unique = list(set(a_long_list))

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# 3. Кастомная реализация sum
print('Кастомная реализация sum')
start_time = time.monotonic()               # запускаем отсчёт времени

sum_value = 0

for n in a_long_list:
    sum_value += n

print(f'Функция посчитала сумму: {sum_value}')

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# 4. Встроенная функция sum
print('Встроенная функция sum')
start_time = time.monotonic()               # запускаем отсчёт времени

sum_value = sum(a_long_list)
print(f'Функция посчитала сумму: {sum_value}')

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# II. Сортировка: sort() vs sorted()
# 1. Дефолтная сортировка с использованием sorted()
print('Сортировка с использованием sorted()')
start_time = time.monotonic()               # запускаем отсчёт времени

sorted(a_long_list)

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# 2. Дефолтная сортировка с использованием sort()
print('Сортировка с использованием sort()')
start_time = time.monotonic()               # запускаем отсчёт времени

a_long_list.sort()

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')

# III. Литералы вместо функций           
# 1. Создание пустого словаря с помощью dict()
print('Создание пустого словаря с помощью dict()')
start_time = time.monotonic()               # запускаем отсчёт времени

sorted_dict1 = dict()

for key, value in sorted(a_dict.items(), key=lambda item:item[1]):
  sorted_dict1[key] = value

print(f'Прошло {time.monotonic() - start_time} секунд')

# 2. Создание пустого словаря с помощью литерала словаря
print('Создание пустого словаря с помощью литерала словаря')
start_time = time.monotonic()               # запускаем отсчёт времени

sorted_dict2 = {}

for key, value in sorted(a_dict.items(), key=lambda item:item[1]):
  sorted_dict2[key] = value

print(f'Прошло {time.monotonic() - start_time} секунд')
# 3. Создание пустого списка с помощью list()
print('Создание пустого списка с помощью list()')
start_time = time.monotonic()               # запускаем отсчёт времени

list()

print(f'Прошло {time.monotonic() - start_time} секунд')
# 4. Создание пустого списка с помощью литерала списка
print('Создание пустого списка с помощью литерала списка')
start_time = time.monotonic()               # запускаем отсчёт времени

[]

print(f'Прошло {time.monotonic() - start_time} секунд')

# IV. Генераторы списков
# 1. Создание нового списка с помощью цикла for
print('Создание нового списка с помощью цикла for')
start_time = time.monotonic()               # запускаем отсчёт времени

even_num = []
for number in another_long_list:
  if number % 2 == 0:
    even_num.append(number)

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')
# 2. Создание нового списка с помощью генератора списка
print('Создание нового списка с помощью генератора списка')
start_time = time.monotonic()               # запускаем отсчёт времени

even_num = [number for number in another_long_list if number % 2 == 0]

print(f'Прошло {(time.monotonic() - start_time):.3} секунд')
