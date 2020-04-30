#! python
# -*- coding: utf-8 -*-

# работа с Turtle

import turtle
import random
import math

PHI = 360 / 7
R = 50
B_X = 100
B_Y = 100


def gotoxy(x, y):
    """Перемещение на координаты x, y"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    """Рисуем круг заданного размера и цвета"""
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_pistol(base_x, base_y):
    """Рисуем пистолет"""
    # рисуем основной кргу
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # рисуем мушку
    gotoxy(base_x, base_y + 160)
    draw_circle(5, 'red')
    # отрисовка барабана
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R,
               base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "white")


def rotate_pistol(base_x, base_y, start):
    """Анимация вращения барабана"""
    for i in range(start, random.randrange(7, 80)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R,
               base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")
    # закращиваем крайний круг - помещаем патрон
    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, 'brown')
    return i % 7    # запоминаем начальную позицию


if __name__ == '__main__':
    turtle.speed(0)     # начальная скорость

    draw_pistol(B_X, B_Y)       # рисуем пистолет

    answer = ''
    start = 0   # стартовая позиция барабана

    while str.lower(answer) != 'n':
        answer = turtle.textinput("Играем?", "(y/n)")
        if str.lower(answer) == 'y':
            start = rotate_pistol(B_X, B_Y, start)
            # проверяем нахождения патрона под мушкой - произощел выстрел
            if start == 0:
                gotoxy(-150, 250)
                turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
        else:
            pass
