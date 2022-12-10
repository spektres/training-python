#Наследование - super

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p): # Добавляем еще одно свойство
        super().__init__(color, param_1, param_2) # Super вызывает init метод из род.класса
        self.rectangle_p = rectangle_p # и добавляет параметр в инициализацию

    
    def get_r_p(self):
        return self.rectangle_p