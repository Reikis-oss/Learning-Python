"""
Задача 10: 
На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.

Input: 
    5 -> 1 0 1 1 0
Output: 
    120 
"""
import random

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

coins = VerificationInt("Введите количество монет: ")
money =  []

for i in range(coins):
    money += [random.randint(0, 1)]
    print(money[i], end= " ")    
print(end="\n")

heads = 1
tails = 0


if money.count(tails) > money.count(heads):
    print(f"На столе больше решек поэтому нужно перевернуть {money.count(heads)} орлов")
elif money.count(tails) < money.count(heads):
    print(f"На столе больше орлов поэтому нужно перевернуть {money.count(tails)} решек")
else:
    print(f"На столе поровну орлов и решек поэтому нужно перевернуть {money.count(heads)} орлов или решек")
