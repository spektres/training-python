numbers_list = []

for _ in range(5):
    numbers_list.append(int(input("Введите число: ")))

print(f"Максимальное число списка {numbers_list} -> {max(numbers_list)}")

