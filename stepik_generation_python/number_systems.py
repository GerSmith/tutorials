#! python
# -*- coding: utf-8 -*-

"""
Работа с системами счисления
"""

n = 0b111111
print(int(n))
# print(int(0b111111))
n = 0x1af2
print(int(n))
n = 1000
print(hex(n))
n = 513
print(bin(513))


num = 127

bin_num = bin(num)  # 0b1111111
oct_num = oct(num)  # 0o177
hex_num = hex(num)  # 0x7f

print(bin_num[2:])  # 1111111
print(oct_num[2:])  # 177
print(hex_num[2:].upper())  # 7F
