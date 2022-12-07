# class Auto:
#     auto_count = 0

#     def on_auto_start(self, auto_name, auto_model, auto_year): #Вместо этого метода обычо используют конструктор
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year

# a = Auto()
# a.on_auto_start("Audi", "A4", 2015)
# print(a.auto_name)
# print(a.auto_model)
# print(a.auto_year)


# b = Auto()
# b.on_auto_start("BMW", "M5", 2018)
# print(b.auto_year)

class Auto:
    
    auto_count = 0
    
    def __init__(self, auto_name, auto_model, auto_year) -> None:
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1

print(Auto.auto_count)
a = Auto("Audi", "RW6", "2016")
print(Auto.auto_count)
b = Auto("Audi", "RW6", "2020")
print(Auto.auto_count)
print(a.auto_year, b.auto_year, b.auto_count)