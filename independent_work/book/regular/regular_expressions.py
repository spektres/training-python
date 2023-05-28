import re

#ignore register
"""p = re.compile(r"^[a-z]+$", re.I)
print("Haйдeнo" if p.search("ABC") else "Not found")"""

"""Найдено, хотя в строке символы в верхнем регистре, а в 
шаблоне - в нижнем """


#Точка не соответствует \n 
"""р = re.compile(r"л.+$") 
p.findall("s1\ns2\ns3") """

# Точка соответствует \n 
"""р = re.compile(r"л.+$", re.S) 
p.findall("s1\ns2\n\s3") """

"""Привязка к началу или концу строки используется, только если 
строка должна полностью соответствовать регулярному выражению. """

p = re.compile(r"^[0-9]+$", re.S) 
num = "123" 
snum = "s123" 
if p.search(num): 
    print("Чиcлo") 
else: 
    print("Cтpoкa") 
if p.search(snum): 
    print("Чиcлo") 
else: 
    print ("Строка") 