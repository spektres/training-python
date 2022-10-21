# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input("Введите колличество элементов: "))
number_list = []

for i in range(n):
    number = int(input(f"Введите {i + 1}-е число: "))
    number_list.append(number)

new_list = []

for i in range((n - 1) // 2 + 1):
    number1 = number_list[i]
    number2 = number_list[n - i - 1]
    new_list.append(number1 * number2)

print(new_list)
