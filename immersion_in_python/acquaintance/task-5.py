n = int(input("n: "))

if (n % 5 == 0 or n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print("Yes")
else: print("No")