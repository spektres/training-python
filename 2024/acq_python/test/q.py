number_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
uniq_list = []

for i in range(len(number_list)):
    if number_list[i] not in uniq_list:
        uniq_list.append(number_list[i])

print(uniq_list)