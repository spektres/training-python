# модуль импорта данных 

def import_data(data):
    with open('company.csv', 'a+', encoding='utf-8') as file:
        file.write("*".join(data))
        file.write(f"\n")