"""Упражнение 6. Налоги и чаевые

(Решено. 17 строк)

Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. 
После этого должен быть произведен расчет налога и  чаевых официанту. 
Вы можете использовать принятую в вашем регионе налоговую ставку для подсчета суммы сборов. 
В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога. 
На выходе программа должна отобразить отдельно налог, сумму чаевых и итог,
включая обе составляющие. Форматируйте вывод таким образом, чтобы
все числа отображались с двумя знаками после запятой."""

price_order = float(input("Сумма заказа: "))
tips = price_order * 0.18
tax = (price_order - tips) * 0.05

print("Сумма заказа: %.2f, чаевые: %.2f, налог: %.2f, прибыль заведения: %.2f" % (price_order, tips, tax, 
                                                                                  price_order - tips - tax))


"""# Вычисляем налог и сумму чаевых в ресторане
#
TAX_RATE = 0.05
TIP_RATE = 0.18

В моем регионе налог составляет 5 %. В языке Python 5 % и 18 % представляются как
0.05 и 0.18 соответственно.

# Запрашиваем сумму счета у пользователя
cost = float(input("Введите сумму счета: "))

# Вычисляем сумму налога и чаевых
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip
# Отобразим результат
print("Налог составил %.2f, чаевые – %.2f, общая сумма заказа: %.2f" % (tax, tip, total))"""