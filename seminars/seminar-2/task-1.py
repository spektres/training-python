# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите число: "))
x = 1

for i in range(1, n):
    x = x * (-3)
    print(x, end=", ")

# n = int(input())
# a = []
# for i in range(n):
#     a.append((-3) ** i)
# print(*a, sep=', ')