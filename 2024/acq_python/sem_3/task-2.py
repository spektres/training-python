

"""    Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

list_number = [2, 3, 4, 5, 6]
len_index = len(list_number)
list_mult = []

if len_index % 2:
    for i in range(len_index // 2 + 1):
        list_mult.append(list_number[i] * list_number[len_index - i -1])
else:
    for i in range(len_index // 2):
        list_mult.append(list_number[i] * list_number[len_index - i -1])

print(list_mult)
