"""Упражнение 22. Площадь треугольника (снова)

(16 строк)

В предыдущем упражнении мы вычисляли площадь треугольника при известных длинах его основания и высоты. Но можно рассчитать площадь
и на основании длин всех трех сторон треугольника. Пусть s1, s2 и s3 – длины сторон, а s = (s1 + s2 + s3)/2. Тогда площадь треугольника может быть
вычислена по следующей формуле:
Разработайте программу, которая будет принимать на вход длины всех
трех сторон треугольника и выводить его площадь."""

from cmath import sqrt


s1, s2, s3 = float(input("s1: ")), float(input("s2: ")), float(input("s3: "))

s = (s1 + s2 + s3) / 2

area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print(area)