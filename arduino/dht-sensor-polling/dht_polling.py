#! python
# -*- coding: utf-8 -*-

"""Тестовый пример обещния (запрос-ответ) по COM-порту с платой Arduino."""

import sys
import time
import serial


def get_time() -> str:
    """Функция возвращает текущее время в читаемом формате."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_value() -> str:
    """Запрос данных по открытому COM-порту."""
    srl.write(b'g')
    arduino_data = srl.readline().decode().split()
    # return arduino_data[0]
    # arduino_data = srl.readline()
    return arduino_data[0], arduino_data[1]


# объявляем настройки (взяты как настройки по умолчанию)
# источник из github.com/WaveShapePlay/ArduinoPySerial_LearningSeries
srl = serial.Serial('COM5', baudrate=9600, timeout=1)
time.sleep(3)

# Выводим сообшение если порт открыт
if srl.is_open:
    print(f'Serial port open at {srl.name}')
# основной цикл - опрашиваем нужно ли взять данные
while True:
    USER_INPUT = input('get some data? (y/n): ')
    if USER_INPUT == 'y':
        print(f'{get_time()} - {get_value()}')
    else:
        sys.exit()  # выход
