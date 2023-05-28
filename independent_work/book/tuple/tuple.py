import itertools as it

a = 1,2,3,4,"d",3,4,6
print(list(it.combinations_with_replacement(a, 2))) # с повторяющимися элементами
print(len(list(it.combinations_with_replacement(a, 2))))

print(list(it.combinations(a, 2)))
print(len(list(it.combinations(a, 2))))