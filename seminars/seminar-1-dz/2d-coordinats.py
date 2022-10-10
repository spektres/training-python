from os import system
from math import sqrt

system('cls')


print("Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.")

print("Введите координаты точки A: ")
ax = float(input("X = "))
ay = float(input("Y = "))
print("Введите координаты точки B: ")
bx = float(input("X = "))
by = float(input("Y = "))

print("Дистанция между точками A и B равна: ", round(sqrt((ax - bx)**2 + (ay - by)**2), 2))
