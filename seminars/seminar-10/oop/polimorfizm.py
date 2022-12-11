# Полиморфизм. Результат работы метода зависит от входных параметров.
# (От из колличества, типа)

class Auto:
    def auto_start(self, param_1, param_2 = None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)