"""Упражнение 24. Единицы времени

(22 строки)

Создайте программу, в которой пользователь сможет ввести временной
промежуток в виде количества дней, часов, минут и секунд и узнать общее
количество секунд, составляющее введенный отрезок."""

day = int(input("days: "))
hours = int(input("hours: "))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))

result = seconds + minutes * 60 + hours * 3600 + day * 864006

print("{} seconds.".format(result))