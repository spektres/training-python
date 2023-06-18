"""Упражнение 31. Единицы давления

(17 строк)

В данном задании вам предстоит написать программу, которая будет переводить введенное 
пользователем значение давления в  килопаскалях
(кПа) в фунты на квадратный дюйм (PSI), миллиметры ртутного столба
и  атмосферы. Коэффициенты и  формулы для перевода найдите самостоятельно."""

CONST_PSI = 6.895

kpa = float(input("KPa = "))

psi = kpa / CONST_PSI
mrs = kpa * 760 / 101.325
atm = kpa / 101.325

print(psi, mrs, atm, sep="++++++++")