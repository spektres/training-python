# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#
# *Примеры:*
#
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = input("ведите число: ")

if "." in number:
    drob = number.split(".")
    print(f"Первая цифра дробной части числа {number} является: {drob[1][0:1]}")
else: print(f"Число {number} не имеет дробной части")

# n = input()
# if '.' in n:
# index_t = n.find('.')
# print(n[index_t + 1])
# else:
# print('нет')