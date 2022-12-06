from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def welcome():
    print("*"*70)
    print("Добро пожаловать в информационню систему MyCompany!")
    print("*"*70)

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона контакта: ")
    post = input("Введите должность: ")
    income = input("Укажите заработную плату: ")
    return [last_name, first_name, middle_name, phone_number, post, income]


def menu():
    print("-"*70)
    print("Доступные операции с MyCompany:\n\
    1 - Добавить сотрудника\n\
    2 - Показать всех сотрудников\n\
    3 - Поиск сотрудника по параметрам\n")
    print("-"*70)
    
    choice = input("Введите цифру: ")
    if choice == '1':
        print('\n ДОБАВИТЬ СОТРУДНИКА: \n')
        import_data(input_data())
        print("-"*70)
        print("ЗАПИСЬ СОЗДАНА")
        print("-"*70)
        menu()
    elif choice == '2':
        print('\n ПОКАЗАТЬ ВСЕХ СОТРУДНИКОВ: \n')
        data = export_data()
        print_data(data)
        menu()
    elif choice == '3':
        print('\n ПОИСК СОТРУДНИКА ПО ПАРАМЕТРАМ: \n')
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Телефон".center(15), "Должность".center(15), "Зарплата".center(30))
            print("-"*100)
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(30))
            menu()
        else:
            print("Данные не обнаружены")
            menu()
    else:
        menu()
