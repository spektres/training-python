# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input("Введите колличество элементов: "))
number_list = []

for i in range(n):
    number = input(f"Введите {i + 1}-е число: ")
    number_list.append(number)
min = 9
max = 0

for el in number_list:
    if '.' in str(el):
        drob = el.split('.')[1]
        if float('0.' + drob) > max:
            max = float('0.' + drob)
        elif float('0.' + drob) < min:
            min = float('0.' + drob)

print(max - min)
