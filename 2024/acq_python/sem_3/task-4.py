

"""    Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

number = int(input('->->->->->'))
binary_str = ''

while number != 0:
    binary_str += str(number % 2)
    number //= 2

print(binary_str[::-1])