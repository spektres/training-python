# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

main_text = input("Введите исходный текст: ")
del_text = input("Введите удаляемую подстроку: ")

def new_text(main_text, del_text):
    new_str = main_text.replace(del_text, "")
    return new_str

print(new_text(main_text, del_text))