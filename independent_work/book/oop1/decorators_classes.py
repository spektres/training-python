"""Начиная с Python 3, кроме декораторов функций поддерживаются 
также декораторы классов, позволяющие изменить поведение обычных 
классов. В качестве параметра декоратор принимает ссылку на 
объект класса, поведение которого необходимо изменить, и должен 
возвращать ссылку на тот же класс или какой-либо другой. Пример:"""

def deco (d): 
    print("Дeкopaтop") 
    return d 

@deco 
class SampleClass: 
    def __init__ (self, value): 
        self.v = value 

оbj = SampleClass(1) 
print(оbj.v) 