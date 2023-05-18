"""from re import *
p = compile('[0-9]+')
print("Haйдeнo" if p.match("s123") else "Не найдено")
print("Haйдeнo" if p.match("123s") else "Не найдено")


р = compile('[0-9]+')
print("Haйдeнo" if p.search("s123") else "Не найдено")
print("Haйдeнo" if p.search("123s") else "Не найдено")"""

# Code check email
import re 
email = "mark@sales.example.com" 
pattern = r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$" 
p = re.compile(pattern, re.I | re.S) 
m = p.search(email)
if not m: 
    print("He совпадает") 
else: 
    print("Совпадает") 