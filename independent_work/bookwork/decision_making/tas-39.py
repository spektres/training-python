"""Упражнение 39. Сколько дней в месяце?

(Решено. 18 строк)

Количество дней в месяце варьируется от 28 до 31. Очередная ваша про-
грамма должна запрашивать у пользователя название месяца и отобра-
жать количество дней в нем. Поскольку годы мы не учитываем, для фев-
раля можно вывести сообщение о том, что этот месяц может состоять как
из 28, так и из 29 дней, чтобы учесть фактор високосного года."""


##
# Определяем количество дней в месяце
#
# Запрашиваем у пользователя название месяца
month = input("Введите название месяца: ")
# Вычисляем количество дней в месяце
days = 31
"""Изначально считаем, что в месяце 31 день, после чего постепенно корректируем это
предположение."""
if month == "Апрель" or month == "Июнь" or \
month == "Сентябрь" or month == "Ноябрь": days = 30
elif month == "Февраль": days = "28 или 29"
"""Для февраля присваиваем переменной days строковое значение. Это позволит нам
вывести информацию о том, что в этом месяце количество дней может варьироваться."""
# Выводим результат
print("Количество дней в месяце", month, "равно", days)