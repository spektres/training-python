"""Условие задачи:

Введите с клавиатуры список с различными значениями (цифры, слова, символы). 
Необходимо проверить, есть ли в этом списке два слова подряд и вывести их на экран. 
Если таких пар нет, то выведите фразу “Мало слов!”.

Sample Input:

Привет пока 12 когда 11 что где 

Sample Output:

Привет пока
что где

"""

word_list = input().split()
words = []
flag = False

for word in word_list:
    if word.isalpha():
        words.append(word)
        if len(words) == 2:
            flag = True
            print(" ".join(words))
            words.clear()
        if not word.isalpha():
            words.clear()
    else: words.clear()


if not flag:
    print("Мало слов!")