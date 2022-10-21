# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from unittest import result


number = int(input("Введите число: "))
res = ''
while number != 0:
    res = str(number % 2) + res
    number //= 2
print(res)
