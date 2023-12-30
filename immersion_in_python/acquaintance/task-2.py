num = 0

for _ in range(5):
    digit = int(input("digit: "))
    if num < digit:
        num = digit

print(num)