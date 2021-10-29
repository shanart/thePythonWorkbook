# Напишите функцию, принимающую на вход длины двух катетов прямо-
# угольного треугольника и возвращающую длину гипотенузы, рассчитан-
# ную по теореме Пифагора. В главной программе должен осуществляться
# запрос длин сторон у пользователя, вызов функции и вывод на экран
# полученного результата.

from math import sqrt


def calc_hypotenuse(cathetus1, cathetus2) -> float:
    return sqrt(cathetus1 ** 2 + cathetus2 ** 2)


if __name__ == '__main__':
    cat1 = int(input('Enter cathetus 1: '))
    cat2 = int(input('Enter cathetus 2: '))
    print('Hypotenuse is: ' + str(calc_hypotenuse(cat1, cat2)))
