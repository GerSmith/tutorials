#! python
# -*- coding: utf-8 -*-

"""Тестовый пример обещния (прослушка) по COM-порту с платой Arduino."""

import time
import serial

# объявляем настройки (взяты как настройки по умолчанию)
# источник из github.com/WaveShapePlay/ArduinoPySerial_LearningSeries
srl = serial.Serial('COM5', baudrate=9600, timeout=1)
time.sleep(3)

# Выводим сообшение если порт открыт
if srl.is_open:
    print(f'Serial port open at {srl.name}')

# Транслируем данные из порта в консоль
while True:
    arduino_data = srl.readline().decode().split()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), arduino_data)
    # time.sleep(0.1)
