numbers = [1,1,2,2,3,4,5,6,6,7,7]
not_unic = []

for digit in numbers:
    if numbers.count(digit) > 1 and digit not in not_unic:
        not_unic.append(digit)

print(not_unic)