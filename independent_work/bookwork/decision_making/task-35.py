"""Упражнение 35. Чет или нечет?

(Решено. 13 строк)

Напишите программу, запрашивающую у пользователя целое число и вы-
водящую на экран информацию о том, является введенное число четным
или нечетным."""

"""number = int(input("num = "))

if number % 2 == 0: print("Yes")
else: print("No")"""


##
# Определяем и выводим на экран информацию о том, четное введенное число или нечетное
#
# Запрашиваем целое число у пользователя
num = int(input("Введите целое число: "))
# Используем оператор взятия остатка от деления
if num % 2 == 1:
   print(num, "нечетное.")
else:
   print(num, "четное.")