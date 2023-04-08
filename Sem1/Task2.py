"""
Задача 2:
Найдите сумму цифр трехзначного числа.

Input: 123
Output: 6 (1 + 2 + 3)

Input: 100 
Output: 1 (1 + 0 + 0)
"""

num = input("Введите число: ")
sum = 0

for i in range(len(num)):
    sum += int(num[i])

print(f"Сумма цифр в числе {num} = {sum}")
