dic1 = dict()
print(dic1)

dic2 = dict(name = "ivan", surname = "ivanov")
print(dic2["name"])

dic3 = dict({"name": "ivan", "surname": "ivanov"})
print(dic3)

dic4 = dict([["name", "Иван"], ["surname", "Иванов"]])
print(dic4)

dic5 = dict([("name", "Иван"), ("surname", "Иванов")])
print(dic5)

"""Первый оператор создает пустой словарь. 
Второй - создает словарь 
по парам Ключ=Значение. 
Третий оператор - создает словарь по 
словарю, да в качестве параметров 
функции dict() мы передали уже 
готовый словарь. 
Четвертый оператор создает словарь 
по списку списков, а пятый - по 
списку кортежей. 
Как видите, существуют различные 
способы создания словарей, и вы 
можете выбрать тот, который вам 
больше нравится."""

import copy
dic6 = copy.deepcopy(dic5) # глубокое копирование. Поверхностное - метод copy
print(dic6)

print(len(dic6))
print("name" in dic6)

for key in dic6.keys(): 
    print("({0} => {1})".format(key, dic6[key]), end=" ") 
    print(key, dic6[key]) 