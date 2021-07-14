#! python
# -*- coding: utf-8 -*-

"""Кремниевая долина."""


# int: echo "6" "222anton456" "a1n1t1o1n1" "0000a0000n00t00000o000000n"
#    "gylfole" "richard" "ant0n" | python .\silicon_valley.py
# out: 1 2 3

n = int(input())  # количество холодильников
frigs = [input() for _ in range(n)]  # список холодильников
# print(n, frigs)


def check_frig(frig: str) -> bool:
    """Ищем в строке frig любой символ из ключа key."""
    key = "anton"  # ключевое слово
    # список "инфицированных" индексов
    infected_idx = [0]  # ноль нужен для поиска
    infected_word = ""  # строка для проверки
    # проверяем вхождение символов их ключа в frig
    for k in key:
        if k not in frig:
            return False
        else:
            idx = frig.find(k, infected_idx[-1])
            if idx != -1:  # если такого значения нет
                infected_idx.append(idx)
    # print(infected_idx)
    # убираем первый индекс - поисковой "0"
    infected_idx.remove(0)
    # print(infected_idx)
    # формируем слово из полученных индексов
    for i in infected_idx:
        infected_word += frig[i]
    # возвращаем True если строка frig заражена key
    # print(infected_word)
    return infected_word == key


# проверка работы функции check_frig
# print(check_frig('222anton456'),
#       check_frig('a1n1t1o1n1'),
#       check_frig('0000a0000n00t00000o000000n'),
#       check_frig('gylfole'),
#       check_frig('richard'),
#       check_frig('ant0n'),
#       check_frig("aoooooooooontooooo"),
#       check_frig(
#           "osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen"),
#       check_frig("anton"),
#       check_frig("aoooooooooontooooo"),
#       check_frig("elelelelelelelelelel"),
#       check_frig("ntoneeee"),
#       check_frig("tonee"),
#       check_frig("253235235a5323352n25235352t253523523235oo235523523523n"),
#       check_frig("antoooooooooooooooooooooooooooooooooooooooooooooooooooon"),
#       check_frig("unton"), sep='\n')

for frig_idx, frig_val in enumerate(frigs):
    if check_frig(frig_val):
        print(frig_idx + 1, end=' ')
