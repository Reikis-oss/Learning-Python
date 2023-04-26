"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел.
 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*
2 2
    4 
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


def the_sum_of_two_int(num1, num2):
    if num2:
        num1 += 1
        return the_sum_of_two_int(num1, num2 - 1)
    else:
        return num1


numer1 = verification_int("Введите первое число: ")
numer2 = verification_int("Введите второе число: ")
print(f" {numer1} + {numer2} = {the_sum_of_two_int(numer1, numer2)}")
