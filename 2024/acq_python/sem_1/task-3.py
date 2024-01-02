"""def diapozon(number):
    maxx = number
    minn = number * -1
    number_list = []
    for i in range(minn, maxx + 1):
        number_list.append(i)
    return number_list

print(diapozon(int(input("Enter number:"))))"""

number = int(input("Enter number: "))

for i in range(number * -1, number + 1):
    print(i, end=", ")



