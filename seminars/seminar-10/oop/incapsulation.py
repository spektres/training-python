# incapsulation - инкапсуляция

class Auto:
    def __init__(self) -> None:
        print('Автомобиль заведен')
        self.auto_name = 'mazda' # Публичный модификатор доступа
        self._auto_year = 2019 # Защищенный модификатор доступа (условно: нежелательно менять)
        self.__auto_model = "CX9" # Приватный модификатор доступа (условно: нельзя менять)

    def __name(self):# С МЕТОДАМИ АНАЛОГИЧНО!
        print(self.auto_name)

a = Auto()
print(a.auto_name)
print(a._auto_year)
# print(a.__auto_model) # Выдаст ошибку
print(a._Auto__auto_model) # Так можно получить доступ

