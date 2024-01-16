def sequence(n):
    first_number = 5
    prir = 8
    second_number = 1
    result_list = ['5:1']
    for _ in range(n):
        first_number -= (prir * 3)
        second_number *= 9
        result_list.append(str(first_number) + ':' + str(second_number))
    return result_list

n = int(input('Number: '))
print(sequence(n))