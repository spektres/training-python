def sequence_dict(n):
    some_dict = {}
    for i in range(1, n + 1):
        some_dict[i] = 3 * i + 1
    return some_dict


print(sequence_dict(int(input('Number: '))))