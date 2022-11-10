# рандомое перемешивания списка (по алгоритмам)

import time
random_number = str(time.time()).split('.')[1]
some_list = [1, 4, 9, 10]
for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
    i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
    time.sleep(0.00001)
    i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
    some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
print(some_list)