"""Упражнение 32. Сумма цифр в числе

(18 строк)

Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую 
сумму составляющих его цифр. Например, если пользователь введет число 3141, программа должна вывести
следующий результат: 3 + 1 + 4 + 1 = 9."""

num = int(input("num = "))

sum_string = ""
sum_digits = 0

while num > 0:
    digit = num % 10
    if not sum_string: sum_string += str(digit)
    else: sum_string += " + " + str(digit)
    sum_digits += digit
    num //= 10

print(sum_string, "=", sum_digits)
