number = int(input("Number: "))

if (number % 5 == 0 or number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
    print("ok")
else: print("no")