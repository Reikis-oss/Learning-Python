"""
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
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


first_element = verification_int("Введите первое число в последовательности: ")
sequence_step = verification_int("Введите шаг последовательности: ")
amount_of_elements = verification_int("Введите количество элементов: ")

for i in range(amount_of_elements):
    print(first_element + i * sequence_step, end='\n')