#! python
# -*- coding: utf-8 -*-

"""Запрос измрений температы с платы Arduino и запись в файл."""

import os
import sys
import time
import serial

TARGET_DIR = 'C:\\TEMP\\Arduino'


def get_time() -> str:
    """Функция возвращает текущее время в читаемом формате."""
    return time.strftime('%Y-%m-%d %H:%M:%S')


def get_values() -> list:
    """Запрос данных по открытому COM-порту."""
    srl.write(b'g')
    # arduino_data = srl.readline().decode().split()
    # return arduino_data[0]
    arduino_data = srl.readline().decode().split()
    return ' '.join(arduino_data)


def check_journal_dir() -> None:
    """Проверяем создана ли директория для хранения журнала измерений."""
    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)
        print('Директория для хранения журанала измрений успешно создана!')
    print(f'Директория хранения журанала измрений: {TARGET_DIR}')


def create_journal_name() -> str:
    """Создаём имя журнала: абсолютный путь до файла измерений."""
    # формат представления '%Y%m%d_%H%M%S.log
    today = time.strftime('%Y%m%d') + '_' + time.strftime('%H%M%S')
    target_name = TARGET_DIR + os.sep + today + '.log'
    print(f'Имя журнала измерений: {target_name}')
    return target_name


def serial_init() -> serial:
    """Инициализация последовательного порта передачи данных."""
    ser = serial.Serial('COM5', baudrate=9600, timeout=1)
    # Выводим сообшение если порт открыт
    if ser.is_open:
        print(f'COM порт открыт: {ser.name}')
        return ser


if __name__ == '__main__':
    # объявляем настройки (взяты как настройки по умолчанию)
    srl = serial_init()
    time.sleep(3)
    # проверяем создан ли каталог для хранения журнала
    check_journal_dir()
    # формируем имя журнала
    journal_name = create_journal_name()
    # записываем вывод скрипта в файл
    while True:
        try:
            # запись осуществляем каждую минуту
            if time.strftime('%S') == '00':
                # файл открывается в режиме для добавления данных
                with open(journal_name, 'a+', encoding='utf-8') as target_file:
                    # записать данные
                    target_file.write(f'{get_time()} - {get_values()}\n')
        except KeyboardInterrupt:
            # перехват закрытия скрипта с клавиатуры
            print('<кто-то закрыл программу>')
            # закрываем порт и выходим
            srl.close()
            sys.exit()
