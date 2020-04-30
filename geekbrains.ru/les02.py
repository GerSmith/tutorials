#! python
# -*- coding: utf-8 -*-

import os
import psutil   #сторонний пакет, устанавливается через pip install psutil
import sys
import platform
import shutil

print("Здравствуйте!")

name = input("Скажите, как Вас зовут? \n")
print(name, ", добро пожаловать в мир Python!")
print("Если хотите выйти наберите <q>, <quit> или <exit>")
answer = ""

while str.lower(answer) != "q" and str.lower(answer) != "quit" and str.lower(answer) != "exit":

    answer = input("Давайте поработаем? (Д/н) ")

    if str.lower(answer) == "д" or str.lower(answer) == "да":
        print("Это здорово, Хозяин!")
        print("Я умею:")
        print(" [1] - вывести список файлов")
        print(" [2] - вывести информацию о системе")
        print(" [3] - выведу список прцоессов")
        print(" [4] - продублирую файлы в текущей директории")
        print(" [5] - удалю продублированные файлы в текущей директории")
        do = int(input("Укажите номер действия "))
        if do == 1:
            print("Текущая директория: ", os.getcwd())
            print(os.listdir())
        elif do == 2:
            print("Текущий пользователь: ", os.getlogin())
            print("Количество ЦП: ", os.cpu_count())
            print("Платформа ОС: ", sys.platform)
            print("Версия ОС: ", platform.win32_ver())
            print("Кодировка ФС: ", sys.getfilesystemencoding())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    if file_list[i][0] != '.':
                        newfile = file_list[i] + '.dupl'
                        shutil.copy(file_list[i], newfile)# коприуй
                i = i + 1
        elif do == 5:
            print("=Удаление продублированных файлов в текущей директории=")
            file_to_remove = os.listdir()
            j = 0
            while j < len( file_to_remove):
                if '.dupl' in file_to_remove[j]:
                    os.remove(file_to_remove[j])
                j = j + 1
        else:
            print("Ты уж определись!")
    elif str.lower(answer) == "н" or str.lower(answer) == "нет":
        print("Очень жаль. Может как-нибудь потом...")
    else:
        print("До свидания!")
