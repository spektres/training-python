# Напишите программу, которая определит позицию второго вхождения строки
# в списке, либо сообщит, что ее нет.


# Алгоритмическое решение

a = []
n = int(input())
for i in range(n):
    a.append(input())
    find_str = input()
count = 0
for el in range(len(a)):
    if a[el] == find_str:
        count += 1
    if count == 2:
        print(el)
    break
else:
    print(-1)


# Решение методами