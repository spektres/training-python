"""Внутри класса можно создать метод, который будет доступен без 
создания экземпляра класса. Для определения статического метода 
используется декоратор @staticmethod."""

class StativSample:
    @staticmethod
    def ssum(x, y):
        return x + y
    def msum(self, x, y):
        return x + y
    
print(StativSample.ssum(2, 2)) # Вызываем до объявления объекта

obj = StativSample()
print(obj.msum(2, 2)) # Вызываем обычный метод
print(obj.ssum(2, 2)) # Вызываем статический метод через объект
    