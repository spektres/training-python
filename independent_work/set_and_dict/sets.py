# Множество - это неупорядоченный набор уникальных элементов.

s = set()
print(s)

s = set("Hello") # Строка
print(s)

s = set([1, 2, 3, 4, 5, 4]) # Список
print(s)

s = set((1, 2, 3, 3, 4, 5)) #Кортеж
print(s)

# Оператор | означает объединение множеств:
 
s1 = set ([ 1, 2, 3]) 
s2 = set([3, 4, 5])
s3 = s1 | s2
print(s3) 

# С помощью | можно добавить в одно множество элементы другого 
# множества: 

s1 |= s2
print(s1)

# Оператор - означает разницу множеств: 

print(s1 - s2)

# Оператор s1 -= s2 удалит из множества s1 элементы, 
# которые существуют и во множестве s1, и во множестве s2. 

s1 -= s2
print(s1)

# Оператор & - это пересечение множеств. Результат пересечения - 
# это элементы, которые есть в обоих множествах:


s1 = set ([ 1, 2, 3]) 
s2 = set([3, 4, 5]) 
print(s1 & s2) 

# Оператор ^ возвращает элементы обоих множеств, 
# исключая одинаковые элементы: 

print(s1 ^ s2)

s1.add(7)
print(s1)