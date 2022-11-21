some_list = ['в', '5', 'часов', '17', 'минут',
             'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(some_list):
    el = some_list.pop(0)
    if el.isdigit():
        some_list.append(f'"0{el}"')
    elif el[0] == "+" and el[1].isdigit():
        some_list.append(f'"+0{el[1:]}"')
    else:
        some_list.append(el)
    i += 1
print(' '.join(some_list))
