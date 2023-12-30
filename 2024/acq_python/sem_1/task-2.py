"""def max_number():
    maxx = 0
    list_number = []
    x = int(input('len numbers: '))
    for i in range(x):
        number = int(input(f'{i + 1} number: '))
        list_number.append(number)
        if maxx < number:
            maxx = number
    return list_number, maxx

result_function = max_number()
print(result_function[0], ' => ', result_function[1])
"""

some_list = map(int, (input('Numbers in line: ').split()))
print(max(some_list))