lst = [1, 2, 3, 4, 5, 6, 7, 8, 3, 0]
lst[::-1] # обратный порядок
lst[:-1] # без последнего элемента
lst[1:] # без первого элемента
lst[0:3] # первые 3
lst[-1:] # последний

lst[1:3] = [8, 9] # изменять элементы списка

lst.append(5) # добавляет элем. в конец
lst += [6, 7] # тоже

lst.insert(0, 0) # Вставили ноль в начало списка 
lst.insert(8, 8) # Вставили 8 в позицию 8 
lst.pop(0) # удаляет элемент с указанным индексом и возвращает его
lst.pop() # удаляет последний элем. и возвр его
del lst[6] # просто удаляет
lst.remove(5) # удаляет эл. с определенным значнием