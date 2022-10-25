# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

n = float(input("Введите число: "))
d = float(input("Введите точность числа: "))
if d == 1: print(int(n))
else:
    d = str(d)
    d = d.split('.')
    d = len(d[1])
    print(round(n, d))