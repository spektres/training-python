"""Упражнение 34. Вчерашний хлеб

(Решено. 19 строк)

Пекарня продает хлеб по $3,49 за буханку. Скидка на вчерашний хлеб составляет 60 %. 
Напишите программу, которая будет запрашивать у пользователя количество приобретенных 
вчерашних буханок хлеба. В вывод на
экран должны быть включены обычная цена за буханку, цена со скидкой
и общая стоимость приобретенного хлеба. Все значения должны быть выведены на отдельных 
строках с соответствующими описаниями. Используйте для вывода формат с двумя знаками после 
запятой и выровненным
разделителем."""

PRICE = 3.49
COEF = 0.6

count = int(input("количество приобретенных вчерашних буханок хлеба: "))

print("Обычная цена: {} \n со скидкой: {}\n стоимость покупки: {}" \
      .format(PRICE, PRICE * COEF, PRICE * count * COEF))