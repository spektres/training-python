# модуль экспорта данных 

def export_data():
    with open('company.csv', 'r', encoding='utf-8') as file:
        data = []

        for line in file:
            temp = line.strip().split('*')
            data.append(temp)

    return data