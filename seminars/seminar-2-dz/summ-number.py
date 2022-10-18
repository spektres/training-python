# - 6782 -> 23
# - 0,56 -> 11

print("Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
number = float(input("Введите число: "))


def summ_number(x):
    if x < 0: x *= -1
    sum = 0
    for i in str(x):
        if i == ".":
            continue
        sum += int(i)
    return sum

print(f"Сумма цифр числа {number} = {summ_number(number)}")
