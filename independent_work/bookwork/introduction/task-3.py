"""Упражнение 3. Площадь комнаты

(Решено. 13 строк)

Напишите программу, запрашивающую у пользователя длину и ширину
комнаты. После ввода значений должен быть произведен расчет площади
комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
в формате числа с плавающей запятой. Дополните ввод и вывод единицами
измерения, принятыми в вашей стране. Это могут быть футы или метры."""

header = "=" * 10 + "Рассчет площади" + "=" * 10
print(header)

width = float(input("Введите ширину в метрах: "))
height = float(input("Введите высоту в метрах: "))
print("Площадь равна {} метров".format(width * height))

print("=" * len(header))