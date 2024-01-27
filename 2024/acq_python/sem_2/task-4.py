

"""    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

    Пример:

- 6782 -> 23
- 0,56 -> 11
"""

"""def sum_digit(float_number: float):
    #Простой алгоритм
    summ = 0
    string_number = str(float_number)
    for i in string_number:
        if not i == '.':
            summ += int(i)
    return summ"""


def sum_digit(float_number: float):
    #Генератор списка
    summ = 0
    summ = summ([int(i) for i in str(float_number) if i != '.'])
    return summ


float_number = float(input("float number: "))

print(sum_digit(float_number))