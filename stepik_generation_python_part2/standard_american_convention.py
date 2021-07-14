#! python
# -*- coding: utf-8 -*-

"""Standard American Convention.

На вход программе подаётся натуральное число.
Программа, вставляет в заданное число запятые в соответствии
со стандартным американским соглашением о запятых в больших числах.
"""

# int: echo "10000000000000000" | python .\standard_american_convention.py
# out: 10, 000, 000, 000, 000, 000

num = int(input())
print('{:,}'.format(num))
