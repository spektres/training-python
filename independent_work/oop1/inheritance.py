# Класс Child унаследовал метод 
# print_name(), который мы можем вызвать из объекта obj. 

class Parent: # Родительский класс 
    def print_name(self): 
        print("Родитель") 
    
class Child(Parent): # Наследование класса Parent 
    def print_child(self): 
        print("Потомок") 
    
obj = Child() 
obj.print_name() 
obj.print_child() 

# Если нужно вызвать именно метод родительского класса, 
# тогда нужно явно указать имя класса:
def print_name(self): 
    print("Потомок") 
    Parent.print_name() 


"""В Python также доступно и множественное наследование - когда 
один Класс наследует атрибуты и методы нескольких классов. Просто нужно указать родительские классы в скобках через запятую: 
class Child(Parentl, Parent2): 
<Определение класса, как обычно>"""