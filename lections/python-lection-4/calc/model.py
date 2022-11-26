x = 0
y = 0

# Метод, отвечающий за инициалиацию чисел (указание нач.знач.)


def init(a, b):
    global x
    global y
    x = a
    y = b

# Метод, складывающий числа


def sum():
    return x + y
