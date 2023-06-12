"""Упражнение 13. Размен

(Решено. 35 строк)

Представьте, что вы пишете программное обеспечение для автоматической кассы в  магазине самообслуживания. 
Одной из функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными.
Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. 
После этого она должна рассчитать и вывести на экран,
сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть 
задействовано минимально возможное количество монет. Допустим, у нас есть в распоряжении монеты достоинством в 1,
5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.
Примечание. Монета номиналом в 1 доллар была выпущена в Канаде в 1987 году.
Свое просторечное название (loonie) она получила от изображения полярной гагары
(loon) на ней. Двухдолларовая монета, вышедшая девятью годами позже, была прозвана toonie, 
как комбинация из слов два (two) и loonie."""

"""change = int(input("Введите сумму сдачи в центах: "))

LOONIE = 100
TOONIE = 200

count_1 = count_5 = count_10 = count_25 = count_loonie = count_toonie = 0

summ = 0

while summ < change:
    if summ + TOONIE < change:
        summ += TOONIE
        count_toonie += 1
        continue
    if summ + LOONIE < change:
        summ += LOONIE
        count_loonie += 1
        continue
    if summ + 25 < change:
        summ += 25
        count_25 += 1
        continue
    if summ + 10 < change:
        summ += 10
        count_10 += 1
        continue
    if summ + 5 < change:
        summ += 5
        count_5 += 1
        continue
    if summ + 1 <= change:
        summ += 1
        count_1 += 1
        continue

print(count_1, count_5, count_10, count_25, count_loonie, count_toonie)"""


#====================================================================
    

##
# Рассчитываем минимальное количество монет для представления указанной суммы
#
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME =10
CENTS_PER_NICKEL =5

# Запрашиваем у пользователя сумму в центах
cents = int(input("Введите сумму в центах: "))

# Определим количество двухдолларовых монет путем деления суммы на 200. Затем вычислим
# оставшуюся сумму для размена, рассчитав остаток от деления
print(" ", cents // CENTS_PER_TOONIE, "двухдолларовых монет")
cents = cents % CENTS_PER_TOONIE

#Деление без остатка в Python выполняется при помощи оператора //. 
# При этом результат всегда будет округлен в нижнюю сторону, что нам и требуется.
# Повторяем эти действия для остальных монет
print(" ", cents // CENTS_PER_LOONIE, "однодолларовых монет")
cents = cents % CENTS_PER_LOONIE
print(" ", cents // CENTS_PER_QUARTER, "25–центовых монет")
cents = cents % CENTS_PER_QUARTER
print(" ", cents // CENTS_PER_DIME, "10–центовых монет")
cents = cents % CENTS_PER_DIME
print(" ", cents // CENTS_PER_NICKEL, "5–центовых монет")
cents = cents % CENTS_PER_NICKEL
# Отобразим остаток в центах
print(" ", cents, "центов")