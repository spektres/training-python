"""Упражнение 8. Сувениры и безделушки

(15 строк)

Интернет-магазин занимается продажей различных сувениров и безделушек. 
Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите программу, запрашивающую у пользователя 
количество тех и других покупок,
после чего выведите на экран общий вес посылки."""

SOUVENIR = 75
TRINKET = 112

print("Общий вес посылки: {}".format(SOUVENIR * int(input("Кол-во сувениров: ")) + 
                                                    TRINKET * int(input("Кол-во безделушек: "))))