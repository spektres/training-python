# inheritance - наследование

class Transport:
    def transport_method(self):
        print("Это родтельский метод из класса Transport")


# Класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
        print("Это метод из дочернего класса")

a = Auto()
a.transport_method()
a.auto_method()