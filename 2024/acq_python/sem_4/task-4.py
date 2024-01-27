"""Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N."""

n = int(input(': '))

delitel = 2

mult_list = []

while n > 1:
    if n % delitel == 0:
        mult_list.append(delitel)
        n //= delitel
    else: 
        delitel += 1

print(mult_list)