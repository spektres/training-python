def thesaurus(*args):
    names = args
    dict_names = {}
    
    for item in names:
        dict_names[item[0]] = item
    return dict_names


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))