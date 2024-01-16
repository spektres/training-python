def len_input(first, second):
    if first < second:
        first, second = second, first
    count_second = first.count(second)
    return count_second


first_string = input('first: ')
second_string = input('sec: ')

print(len_input(first_string, second_string))