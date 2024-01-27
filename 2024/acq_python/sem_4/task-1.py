numbers_str = input(': ').split()

numbers = [int(item) for item in numbers_str]
print(max(numbers), min(numbers))
