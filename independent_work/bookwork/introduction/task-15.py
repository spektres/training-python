"""Упражнение 15. Расстояние

(20 строк)

Для этого упражнения вам необходимо будет написать программу, которая будет запрашивать у 
пользователя расстояние в  футах. После этого
она должна будет пересчитать это число в дюймы, ярды и мили и вывести на экран. 
Коэффициенты для пересчета единиц вы без труда найдете
в интернете."""

feet = int(input("Введите расстояние в футах: "))

print(feet * 12, "дюймов")
print(feet * 0.33, "ярдов")
print(feet * 0.00019, "мили")