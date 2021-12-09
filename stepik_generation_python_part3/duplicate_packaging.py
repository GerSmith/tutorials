#! python
# -*- coding: utf-8 -*-

"""Упаковка дубликатов.

На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности
одинаковых символов заданной строки в подсписки.
"""


# in: echo "w w w o r l d g g g g r e a t t e c c h e m g g p w w" | python duplicate_packaging.py
# out: [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]

row = input().split()  # ввод данных

# print(row, type(row))


def duplicate_packaging(input_row):
    """Упаковка дубликатов.

    Функция принимает строку и формирует
    упакованный список
    """
    row_lst = list()
    row_lst.append([row[0]])

    # print(row_lst, type(row_lst))
    for i in input_row[1:]:
        if i in row_lst[-1][-1]:
            row_lst[-1].extend(i)
        else:
            row_lst.append([i])
    return row_lst


print(duplicate_packaging(row))
