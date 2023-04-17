"""
Задача 14: 
Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.

Input:
    10 

Output:   
    1 2 4 8
"""
import math

# Проверка что пользователь ввёл число
def VerificationInt(mes):
    while True:
        try:
            numer = int(input(mes))       
        except ValueError:
            print("Вы ввели не число. Попробуйте снова!")
            continue
        else:
            return numer

count = VerificationInt("Введите крайнее число в последовательности: ")
i = 0

while True:
    if (counter := int(math.pow(2,i))) <= count:
        print(counter, end=" ")
        i += 1
    else:
        break
    