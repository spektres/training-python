import random

print("Программа загадала случайное чсло от 1 до 100. Попробуйте угадать. Введите число:")
number = random.randint(1, 100)
guess = int()

while guess != number:
    guess = int(input())
    if guess > number: print("Слишком много, попробуйте еще раз")
    elif guess < number: print("Слишком мало, попробуйте еще раз")
    else: print("Вы угадали, поздравляем!")

input('Нажмите ENTER для выхода')
