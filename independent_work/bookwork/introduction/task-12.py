"""Упражнение 12. Расстояние между точками на Земле

(27 строк)

Как известно, поверхность планеты Земля искривлена, и расстояние между точками, характеризующимися одинаковыми градусами по долготе,
может быть разным в зависимости от широты. Таким образом, для вычис-
Введение в программирование  27
ления расстояния между двумя точками на Земле одной лишь теоремой
Пифагора не обойтись.

Допустим, (t1, g1) и (t2, g2) – координаты широты и долготы двух точек на
поверхности Земли. Тогда расстояние в километрах между ними с учетом
искривленности планеты можно найти по следующей формуле:
distance = 6371,01´arccos(sin(t1)´sin(t2) + cos(t1)´cos(t2)´cos(g1 - g2)).

Примечание. Число 6371,01 в этой формуле, конечно, было выбрано не случайно
и представляет собой среднее значение радиуса Земли в километрах.
Напишите программу, в которой пользователь будет вводить координаты двух точек на Земле (широту и долготу) в градусах. На выходе мы
должны получить расстояние между этими точками при следовании по
кратчайшему пути по поверхности планеты.

Подсказка. Тригонометрические функции в  Python оперируют радианами. Таким
образом, вам придется введенные пользователем величины из градусов перевести
в радианы, прежде чем вычислять расстояние между точками. В модуле math есть
удобная функция с названием radians-Функции:radians, служащая как раз для перевода градусов в радианы."""

from math import *

t1 = radians(float(input("t1: ")))
g1 = radians(float(input("t1: ")))
t2 = radians(float(input("t2: ")))
g2 = radians(float(input("t2: ")))

print(t1, g1, t2, g2)


distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(distance)

