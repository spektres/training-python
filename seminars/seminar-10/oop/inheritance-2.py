# Наследование - несколько родителей

class Player:
    def player_method(self):
        print('Родительский метод класса Player')

    def mobile_phone_method(self):
        print('Дочерний метод класса MobilePhone')


class Navigator:
    def navigator_method(self):
        print('Родительский метод класса Navigator')

    def mobile_phone_method(self):
        print('Дочерний метод класса MobilePhone')

# сначала вызывается свой метод, за тем по порядку Player, Navigator
class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print('Дочерний метод класса MobilePhone')


a = MobilePhone()
a.mobile_phone_method()