#! python
# -*- coding: utf-8 -*-

"""Task from Codewars."""


def find_nb(m):
    """Return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m."""
    n = 0
    while True:
        if m < 0:
            return -1
        elif m == 0:
            return n
        else:
            volume = (n + 1) ** 3
            m = m - volume
            n += 1


print(find_nb(1071225))  # 45
print(find_nb(91716553919377))  # -1
print(find_nb(4183059834009))  # 2022
print(find_nb(24723578342962))  # -1
print(find_nb(135440716410000))  # 4824
print(find_nb(40539911473216))  # 3568
print(find_nb(26825883955641))  # 3218
