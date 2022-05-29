#1 Сформировать список из N членов последовательности.
n = int(input('inter number: '))

def progression(n):
    return [((-3) ** i) for i in range(n)]


print(progression(n))

#2 Для натурального n создать словарь индекс-значение,
# состоящий из эелементов последовательности 3n+1.

from random import randint
n = randint(5, 10)

def dictget(n):
    return {x: 3 * x + 1 for x in range(1,  n + 1)}

print(n)
print(dictget(n))


#3 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
String = 'parampampamparampam'
Substring = 'pam'

count = String.count(Substring)

print('Count of pam in parampampamparampam is : ', count)


#4 Подсчитать сумму цифр в вещественном числе
import random

random_number = random.random()
n = (random_number)
print(n)


def sum_digit(n):
    return sum(map(int, list(str(n).replace('.', ''))))
    print(n)


print(sum_digit(n))


# Написать программу получающую набор произведений чисел от 1 до N.

from itertools import accumulate
import operator

N = int(input('inter number: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_prods(N))
