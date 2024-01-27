

"""    Напишите программу, которая принимает на вход число N и выдает набор 
произведений чисел от 1 до N.

    Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

def product_digit(number: int):
    product_list = [1]
    for i in range(1, number):
        step = product_list[i - 1] * (i + 1)
        product_list.append(step)
    return product_list

n = int(input('Number: '))

print(product_digit(n))