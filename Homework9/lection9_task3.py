# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

from pathlib import Path
import re

path_origin = Path("test_file", "task_3.txt")
origin = open(path_origin, mode='r', encoding='utf-8')
purchase_list_str = origin.readlines()  # вычитываем строки с суммами в файле в виде списка сумм

for i in range(len(purchase_list_str)):
    purchase_list_str[i] = purchase_list_str[i][:-1]  # убираем переход на следующую строку \n в списке сумм
    if purchase_list_str[i] != '':  # изменяем тип со строки на число для ненулевых элементов списка
        purchase_list_str[i] = int(purchase_list_str[i])
print(purchase_list_str)

split_purchase_list = [[]]
for i in purchase_list_str:  # разделяем список на подсписки (покупки) с нулевыми строками '' в качестве разделителя
    if i == '':
        split_purchase_list.append([])
    else:
        split_purchase_list[-1].append(i)
print(split_purchase_list)

sum_purchase_list = []
for one_purchase in split_purchase_list:  # вычисляем сумму каждой из покупки из добавляем её в список сумм покупок sum_purchase_list
    sum_purchase_list.append(sum(one_purchase))
print(sum_purchase_list)

sum_purchase_list.sort()  # сортируем список сумм по возрастанию
three_most_expensive_purchases = sum_purchase_list[-1] + sum_purchase_list[-2] + sum_purchase_list[-3]  # суммируем в проверяемой переменной 3-и самые дорогие покупки
print("Сумма 3-х самых дорогих покупок =", three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
