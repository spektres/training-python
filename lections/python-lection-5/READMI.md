# PIP

https://pypi.org/ - Поиск, установка и публикация Python’ьих пакетов в указателе пакетов Python’а

* isOdd - проверка числа на четность

# Установка

pip install isOdd

# Применение

from isOdd import isOdd

print(isOdd('1')) //=> true
print(isOdd('5')) //=> true

print(isOdd(0)) //=> false
print(isOdd(4)) //=> false


python -m venv .folder - команда для создания папки, в которую будут складываться скачиваемые библиотеки. Так же создает виртуальное кружение.
__________________________________

Создание TG-бота:
- https://github.com/python-telegram-bot/python-telegram-bot
- из GH по ссылке: python-telegram-bot.org 
- установка, коп. кода
- ищем BotFather, стартбот, создание, получение токена
- переход в бота, старт
- запускаем main.py