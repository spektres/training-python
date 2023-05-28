class SampleClass:
    def __init__(self):
        print("Constructor")
        self.nm = "SampleClass"
    def printName(self):
        print(self.nm)

obj = SampleClass()
obj.printName()

print(obj.nm)

# озвращает значение атрибута по его названию, 
# которое указывается в виде строки
print(getattr(obj, "nm"))

# setattr() - устанавливает значение атрибута. 
# Название атрибута задается в виде строки
setattr(obj, "nm", "asdvsdv")
print(obj.nm)
setattr(obj, "x", 123)
print(obj.x)

# delattr() - удаляет атрибут, название, 
# как обычно, задается в виде строки
delattr(obj, "nm")

#  hasattr() - проверяет наличие указанного атрибута. 
# Если атрибут существует, возвращается True
print("nm - {0}, x - {1}".format(hasattr(obj, "nm"), hasattr(obj, "x")))
