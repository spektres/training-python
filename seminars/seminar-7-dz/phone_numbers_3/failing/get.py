from failing import saving_data as sd


def searchcontact(): 
    searchname = input("Введите ИМЯ для поиска контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(sd.filename, "r+", encoding='utf-8') 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            found = True
            print("По вашему запросу найден контакт: ", end = " ") 
            while line != "End":
                print(line)
                break 
    if found == False:
        print(f"Контакт {searchname} не найден в справочнике, сожалею")