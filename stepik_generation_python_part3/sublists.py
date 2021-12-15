#! python
# -*- coding: utf-8 -*-

"""Подсписки списка.

На вход программе подается строка текста, содержащая символы.
Из данной строки формируется список. Напишите программу,
которая выводит список, содержащий все возможные
подсписки списка, включая пустой список.
"""


# in: echo "a b v" | python sublists.py
# out: [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

row = input().split()  # ввод данных

# print(row)


def create_sublists(source):
    """Создаём подсписок списка."""
    row_lst = list()

    row_lst.append(list())

    for i in range(1, len(source) + 1):
        print('i = ', i)
        for j in range(0, len(source) + 1 - i):
            print('j = ', j)
            row_lst.append(source[j:j + i])

    return row_lst


print(create_sublists(row))
