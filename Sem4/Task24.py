"""
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

from random import randint


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

def print_list(list1, mes):
    for i in range(len(list1)):
        print(f"{i + 1} {mes} = {list1[i]}")

    print()


max_number_berries = verification_int("Введите максимальное количество ягод на кусте: ")
if max_number_berries < 1:
    print("Введены неправильные значения", "")
    ValueError()
else:
    list_1 = list(randint(1, max_number_berries)
                  for i in range(verification_int("Введите количество кустов: ")))

    selected_bush = verification_int("Введите номер выбранного куста: ") % len(list_1)

    if selected_bush == 1:
        res = list_1[-1] + list_1[0] + list_1[1]
    elif selected_bush == len(list_1):
        res = list_1[len(list_1) - 2] + list_1[len(list_1) - 1] + list_1[0]
    else:
        res = list_1[selected_bush - 2] + list_1[selected_bush - 1] + list_1[selected_bush]

    print("Количество ягод на кустах:")
    print_list(list_1, 'куст: ')
    print(f"Выбранный куст:\n\t {selected_bush}",
          f"Результат сбора:\n\t {res}",
          sep="\n")
