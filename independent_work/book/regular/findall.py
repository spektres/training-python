"""Метод findall() ищет все совпадения с шаблоном.
Если найдены соответствия, то возвращается список с фрагментами, 
в противном случае возвращается пустой список. Если внутри 
шаблона есть несколько групп, то каждый элемент списка будет кортежем, 
а не строкой."""
import re
p = re.compile(r"[a-z]+") 
p.findall("abc, Ьса, 123, dsf") 
#['аЬс', 'Ьса', 'dsf'] 
p.findall("l234, 12345, 123456") 
#[] 