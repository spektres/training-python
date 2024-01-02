number = float(input("Number: "))

tail = number * 10 % 10

if tail == 0:
    print(number, "-> No")
else: print(int(tail), " -> Yes")