first_list = [1, 5, 2, 3, 4, 6, 1, 7]
last_list = []

for i in range(len(first_list)):
    if first_list[i - 1] + 1 == first_list[i]:
        last_list.append(first_list[i - 1])

print(last_list)