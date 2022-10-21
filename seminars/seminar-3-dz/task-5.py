# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from re import I


x = int(input("Введите число: "))
number_list = [0] * (x * 2 + 1)
number_list[x + 1] = 1
for i in range(x + 2, x * 2 + 1):
    number_list[i] = number_list[i - 1]+number_list[i - 2]
for i in range(x, -1, -1):
    number_list[i] = number_list[i + 2]-number_list[i + 1]
print(number_list)
