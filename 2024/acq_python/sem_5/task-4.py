"""Условие задачи:

Напишите функцию с названием detect_lucky, которая принимает в качестве аргумента 
шестизначное число и возвращает True, если оно является счастливым, и False в противном случае. 
Счастливым называется шестизначное число, сумма первых трех цифр которого равна сумме 
последних трех цифр.

Например, число 237831 является счастливым: 2+3+7 = 12 и 8+3+1 = 12. А 12 =12, 
поэтому функция вернет True.

Вызов функции уже прописан. Вам остается написать только саму функцию.

Примечание. Код должен возвращать значение, а не печатать его на экран.

Sample Input:

985778

Sample Output:

True

"""

def detect_lucky(number):
    first_digits = 0
    tail_digits = 0
    while number:
        if number >= 1000:
            tail_digits += number % 10
            number //= 10
        if number < 1000:
            first_digits += number % 10
            number //= 10
        
    if first_digits == tail_digits:
        return True
    else:
        return False



print(detect_lucky(985778))