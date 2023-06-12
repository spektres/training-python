"""Упражнение 18. Объем цилиндра

(15 строк)

Объем цилиндра может быть рассчитан путем умножения площади круга,
лежащего в его основе, на высоту. Напишите программу, в которой пользователь будет 
задавать радиус цилиндра и его высоту, а в ответ получать
его объем, округленный до одного знака после запятой."""

from math import pi

r = float(input("Введите радиус цилиндра: "))
h = float(input("Введите высоту цилиндра: "))

area = pi * (r * r)
volume = (4 / 3 * pi * r**3) * h

print("Объем цилиндра равен {}".format(volume))