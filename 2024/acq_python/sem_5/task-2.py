"""Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет 
нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"""""

import random

def bot_move(confety_left):
    if confety_left <= 28:
        return confety_left
    elif confety_left % 29 == 0:
        return random.randint(1, 28)
    else:
        return confety_left % 29

jer = random.randint(1, 2)
confety_len = 2021
confety_user_1 = 0
confety_user_2 = 0
stepik_user = ''

while confety_len != 0:
    if jer == 1:
        if confety_len > 27:
            if stepik_user == 'user-2':
                bot_choice = bot_move(confety_len)
                confety_user_1 += bot_choice
                confety_len -= bot_choice
                print(f"Бот взял {bot_choice} конфет.")
            else:
                confety_user_1 += int(input("Первый игрок берет конфты: "))
                confety_len -= confety_user_1
            stepik_user = 'user-1'
            jer = 2
            print(f"У игрока 1 {confety_user_1} конфет. Всего осталось: {confety_len}")
        else:
            print("Вы не можете взять конфет больше чем есть!")
    else:
        if confety_len > 27:
            if stepik_user == 'user-1':
                bot_choice = bot_move(confety_len)
                confety_user_2 += bot_choice
                confety_len -= bot_choice
                print(f"Бот взял {bot_choice} конфет.")
            else:
                confety_user_2 += int(input("Второй игрок берет конфты: "))
                confety_len -= confety_user_2
            stepik_user = 'user-2'
            jer = 1
            print(f"У игрока 2 {confety_user_2} конфет. Всего осталось: {confety_len}")
        else:
            print("Вы не можете взять конфет больше чем есть!")

print(f"Выиграл игрок {stepik_user}!")
