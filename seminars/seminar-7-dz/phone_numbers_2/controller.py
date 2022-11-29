from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def welcome():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def menu():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    choice = input("Введите цифру: ")
    if choice == '1':
        print('\n СОЗДАНИЕ КОНТАКТА: \n')
        import_data(input_data())
        menu()
    elif choice == '2':
        print('\n ЭКСПОРТ КОНТАКТОВ: \n')
        data = export_data()
        print_data(data)
        menu()
    elif choice == '3':
        print('\n ПОИСК КОНТАКТА: \n')
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Категория".center(30))
            print("-"*100)
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(30))
            menu()
        else:
            print("Данные не обнаружены")
            menu()
    else:
        menu()