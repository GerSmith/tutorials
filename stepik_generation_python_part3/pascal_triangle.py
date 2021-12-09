#! python
# -*- coding: utf-8 -*-

"""Треугольник Паскаля.

На вход программе подается число n. Напишите программу,
которая возвращает указанную строку треугольника Паскаля
в виде списка (нумерация строк начинается с нуля).
"""


# in: echo "3" | python pascal_triangle.py
# out: [1, 3, 3, 1]

n = int(input())  # ввод данных, n >= 0


def pascal(row_num):
    """Вывод строки треугольника Паскаля.

    Функция принимает номер строки и возвращает
    соответствующую строку треугольника Паскаля
    """
    # создаём треугольник
    triangle = list()
    for i in range(1, row_num + 2):
        triangle.append([1] * i)
    # перебираем треугольник, наполняя его значениями
    for idx, row in enumerate(triangle):
        for pos, _ in enumerate(row):
            if pos not in (0, len(row) - 1):
                # если не первый и не последний элемент,
                # перепаковываем значения по правилу:
                # x[i][j] = x[i-1][j-1] + x[i-1][j]
                triangle[idx][pos] = triangle[idx -
                                              1][pos - 1] + triangle[idx - 1][pos]
    # возвращаем список из треугольника с запрошенной строкой
    # print(triangle) # тестовый вывод
    return triangle[row_num]


print(pascal(n))
