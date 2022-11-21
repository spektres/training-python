# Напишите программу, удаляющую из текста все слова, содержащие подстроку

string_text = input("Введите строку: ").split()
del_text = input("Введите подстроку: ")
new_text = ""

for el in string_text:
    if del_text not in el:
        new_text += el + " "

print(new_text)



