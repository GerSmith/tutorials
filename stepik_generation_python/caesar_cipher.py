#! python
# -*- coding: utf-8 -*-

"""Скрипт шифрует и дешифрует текст в соответствии с алгоритмом Цезаря.

- направление: шифрование или дешифрование
- язык алфавита: русский или английский
- шаг сдвига (со сдвигом вправо)
"""

import string
import re

eng_up_abc = string.ascii_uppercase
eng_low_abc = string.ascii_lowercase
rus_up_abc = ''.join([chr(i) for i in range(1040, 1072)])
rus_low_abc = ''.join([chr(i) for i in range(1072, 1104)])
pow_eng_abc = len(eng_low_abc)
pow_rus_abc = len(rus_low_abc)


def get_shifted_letter(char: str, step: int) -> str:
    """Функция возвращает зашифрованный символ (char)
    сдвинутый на шаг (step) вправо относительно своего алфавита
    """
    if char in eng_up_abc:
        indx = (eng_up_abc.find(char) + step) % pow_eng_abc
        return eng_up_abc[indx]
    elif char in eng_low_abc:
        indx = (eng_low_abc.find(char) + step) % pow_eng_abc
        return eng_low_abc[indx]
    elif char in rus_up_abc:
        indx = (rus_up_abc.find(char) + step) % pow_rus_abc
        return rus_up_abc[indx]
    elif char in rus_low_abc:
        indx = (rus_low_abc.find(char) + step) % pow_rus_abc
        return rus_low_abc[indx]
    else:
        return char


def get_restored_letter(char: str, step: int) -> str:
    """Функция возвращает расшифрованный символ (char)
    сдвинутый на шаг (step) вправо относительно своего алфавита
    """
    if char in eng_up_abc:
        indx = (eng_up_abc.find(char) - step) % pow_eng_abc
        return eng_up_abc[indx]
    elif char in eng_low_abc:
        indx = (eng_low_abc.find(char) - step) % pow_eng_abc
        return eng_low_abc[indx]
    elif char in rus_up_abc:
        indx = (rus_up_abc.find(char) - step) % pow_rus_abc
        return rus_up_abc[indx]
    elif char in rus_low_abc:
        indx = (rus_low_abc.find(char) - step) % pow_rus_abc
        return rus_low_abc[indx]
    else:
        return char


# text = 'Умом Россию не понять'
# text = 'Блажен, кто верует, тепло ему на свете!'
# text = 'To be, or not to be, that is the question!'
# print(*[get_shifted_letter(i, 17) for i in text], sep='')
# text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
# text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
# print(*[get_restored_letter(i, 25) for i in text], sep='')
# text = 'Hawnj pk swhg xabkna ukq nqj.'
# for i in range(0, 26):
    # print(*[get_restored_letter(j, i) for j in text], sep='')

text = 'Day, mice. "Year" is a mistake!'
# len_lst = [len(i) for i in text.split()]
# len_lst = [3, 4, 4, 2, 1, 7]
len_lst = [len(i) for i in re.findall(r'\b\w+\b', text)]
for indx, value in enumerate(text.split()):
    print(*[get_shifted_letter(i, len_lst[indx])
            for i in value], sep='', end=' ')

"""
----- тестовый вывод для отладки -----
print(ord('A'), ord('a'))
print(ord('Z'), ord('z'))

print(' '.join([chr(i) for i in range(65, 91)]))
print(' '.join([chr(i) for i in range(97, 123)]))

print(ord('А'), ord('а'))
print(ord('Я'), ord('я'))

print(' '.join([chr(i) for i in range(1040, 1072)]))
print(' '.join([chr(i) for i in range(1072, 1104)]))

print(eng_up_abc)
print(*[get_shifted_letter(i, 3) for i in eng_up_abc], sep='')
print(eng_low_abc)
print(*[get_shifted_letter(i, 3) for i in eng_low_abc], sep='')
print(rus_up_abc)
print(*[get_shifted_letter(i, 3) for i in rus_up_abc], sep='')
print(rus_low_abc)
print(*[get_shifted_letter(i, 3) for i in rus_low_abc], sep='')
"""
