# Задайте список. Определите, присутствует ли в заданном
# списке строк число.

a = []
n = int(input())
for i in range(n):
    a.append(input())
find_number = input()
for i in a:
    if find_number in i:
        print('да')
    break
else:
    print('нет')