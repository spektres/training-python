from failing import saving_data as sd
from failing import model
from failing import get


print()
print("ТЕЛЕФОННЫЙ СПРАВОЧНИК")

def main_menu(): 
    print( "\nГЛАВНОЕ МЕНЮ\n") 
    print( "1. Просмотреть все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Найти существующий контакт") 
    print( "4. Выход") 
    choice = input("Выберите пункт меню: ") 
    if choice == "1": 
        myfile = open(sd.filename, "r+", encoding='utf-8') 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Искомый контакт не обнаружен, сожалею") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "2": 
        model.newcontact() 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "3": 
        get.searchcontact() 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "4": 
        print("Спасибо, что используете телефонный справочник!") 
    else: 
        print( "Пожалуйста, повторите ввод\n") 
        enter = input("Для продолжения нажмите Enter")
        main_menu()