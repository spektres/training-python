"""import numpy as np

an = np.array([2, 2, 4, 8])
bn = np.array([3, 4, 7, 4])

print(an / bn)"""

import numpy as np

grid = np.zeros(shape=(10, 10), dtype=float)
grid += 12

print(grid)


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1], "ряд 0")
print(a[:,1], "колонка 1")

a[1:3, 1:3] += 10
print(a, "Выбираем фрагмент массива и изменяем его")