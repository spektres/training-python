n = 8
with open('coef.txt', 'r', encoding='utf-8') as k:
    some_list = list(map(int, k.read().split()))

for i in range(n - 1):
    if some_list[i] != some_list[i + 1] - 1:
        print(some_list[i + 1] - 1)