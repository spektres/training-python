"""Упражнение 4. Площадь садового участка

(Решено. 15 строк)

Создайте программу, запрашивающую у  пользователя длину и  ширину
садового участка в футах. Выведите на экран площадь участка в акрах.

Подсказка. В одном акре содержится 43 560 квадратных футов"""

header = "=" * 10 + "Рассчет площади" + "=" * 10
print(header)

width = float(input("Введите ширину в футах: "))
height = float(input("Введите высоту в футах: "))

print("Площадь равна {} акр".format(width * height / 43560))

print("=" * len(header))


"""
SQFT_PER_ACRE = 43560
# Запрашиваем информацию у пользователя
length = float(input("Введите длину участка (футы): "))
width = float(input("Введите ширину участка (футы): "))
# Вычислим площадь в акрах
acres = length * width / SQFT_PER_ACRE
# Отобразим результат
print("Площадь садового участка равна", acres, "акров")
"""