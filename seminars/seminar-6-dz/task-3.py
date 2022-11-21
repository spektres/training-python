list = [57.8, 46.51, 97, 66, 19.48, 83, 33.11, 55, 7.77, 49]

store_id = id(list)
end_word: str = ", "

print("Приведенный к нужному виду список цен: ")

for i, num in enumerate(list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

print("Сптсок цен, отсортированный по возрастанию: ")
list.sort()
print(list)

copy_of_list = list.copy()
copy_of_list.sort(reverse=True)

print("Сптсок цен, отсортированный по убыванию: ")
print(copy_of_list)


print("Цены пяти самых дорогих товаров", list[-6:-1])




