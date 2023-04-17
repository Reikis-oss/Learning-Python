"""
Задача 11
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи (не индекс!) оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input: 
    5
Output: 
    6
"""
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

a = VerificationInt("Введите число: ")
fib = [0, 1]

for i in range(a):
    if fib[i] < a:
        fib += [fib[i]+fib[i+1]]
    else: break

print(f"В последовательности Фибоначчи:\n {fib}")
try:
    print(f"Искомое число является {fib.index(a)+1} по счёту")
except:
    print("Искомого числа нет")
