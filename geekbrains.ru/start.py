#! python
# -*- coding: utf-8 -*-

def sayhello():
    print("Say Hello Kitty!")

def partone():
    print(str(10/3), str(10 // 3), str(10 % 3), str(10 ** 3))

def parttwo():
    print(str(10 * 3 + 1), str(10 * (3 + 1)))

if __name__ == "__main__":
    sayhello()
    partone()
    parttwo()

    name = input("What is your name, Jedi? \n")

    print(name, ", welcome to Python World!")
