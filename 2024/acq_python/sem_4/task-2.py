num_1 = int(input(': '))
num_2 = int(input(': '))

i = 1

while i % num_1 != 0 or i % num_2 != 0:
    i += 1 

print(i)