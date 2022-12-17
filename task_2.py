"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))