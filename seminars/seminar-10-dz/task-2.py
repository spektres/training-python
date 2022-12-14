class Table(): #  создаем класс 
    def __init__(self, x, y): # передаем эеземпляр класса и его параметры в конструктор
        self.x = x  # выдаем полям значения
        self.y = y #выдаем полям значения 
        self.a = [[0] * y for i in range(x)] # залаем поля таблицы генератором
 
    def get_value(self, x, y):
        if 0 <= x < self.x and 0 <= y < self.y: # если x и y  в заданном промежутке, то - передать занчения x и н в массив
            return self.a[x][y]
        else: # иначе вкрнуть None 
            return None
 
    def delete_row(self, row):
        self.a.pop(row) #удаление стррок из массива ы
        self.x -= 1 #удаление конкретно элемнгта, который содержался в ряду
 
    def n_cols(self):# количество столбцов в массиве
        return self.y 
 
    def set_value(self, x, y, a):
        self.a[x][y] = a # перелача значения в них
 
    def n_rows(self):
        return self.x  #количество строк
 
    def add_row(self, row):
        self.a.insert(row, [0] * self.y)# задаем значение(0)
        self.x += 1 #  добавляем строки
 
    def add_col(self, col): # добавленин столбцов
        for row in range(self.x):
            self.a[row].insert(col, 0) 
        self.y += 1
 
    def delete_col(self, y): #удаление 
        for i in range(self.x):
            self.a[i].pop(y) 
        self.y -= 1



tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()