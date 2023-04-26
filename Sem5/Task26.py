"""
Задача 26: 
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
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


def int_pow(num1, num2, res):
    if num2 > 0:
        res *= num1
        return int_pow(num1, num2 - 1, res)
    elif num2 < 0:
        res /= num1
        return int_pow(num1, num2 + 1, res)
    else:
        return res
    


numer1 = verification_int("Введите первое число: ")
numer2 = verification_int("Введите второе число: ")
print(f" {numer1}^{numer2} = {int_pow(numer1, numer2, 1)}")