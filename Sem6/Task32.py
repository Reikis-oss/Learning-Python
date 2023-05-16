"""
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


# Проверка, что пользователь ввёл число
def verification_int(mes):
    while True:
        try:
            numer = int(input(mes))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова!")
            continue
        else:
            return numer


min_num = verification_int("Задайте минимум массива: ")
max_num = verification_int("Задайте максимум массива: ") + 1
int_list = [i for i in range(min_num, max_num)]

minimumLimit = verification_int("Задайте границу минимума искомого диапазона: ")
maximumLimit = verification_int("Задайте границу минимума искомого диапазона: ")

print(int_list)
print(f"Числа лежачие между {minimumLimit} и {maximumLimit} имеют индексы: ")
for i in range(len(int_list)):
    if int_list[i] >= minimumLimit and int_list[i] <= maximumLimit:
        print(i, end=" ")
