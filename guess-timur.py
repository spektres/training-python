import math

print("Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает 'больше' или 'меньше') Руслан может гарантированно угадать число Тимура?")
print("На вход программе подается натуральное число n.")
print("Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура.")
print("Так вот Вы - Тимур. Загадайте число:")

print(math.ceil(math.log2(int(input()))))



