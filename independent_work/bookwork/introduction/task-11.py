"""Упражнение 11. Потребление топлива

(13 строк)

В США потребление автомобильного топлива исчисляется в  милях на
галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель
обычно выражается в  литрах на 100 км (liters-per-hundred kilometers –
L/100 km). Используйте свои исследовательские способности, 
чтобы определить формулу перевода первых единиц исчисления в последние. После
этого напишите программу, запрашивающую у пользователя показатель
потребления топлива автомобилем в америкнских единицах и выводящую его на экран в канадских единицах."""

millle_gal = float(input("Введите кол-во миль на галлон: "))

print("{} литров на 100 км".format(235.22 / millle_gal))