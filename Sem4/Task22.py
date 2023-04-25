"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
    n — кол-во элементов первого множества.
    m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
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


def list_creation(length):
    list1 = []
    for i in range(length):
        list1 += [verification_int(f"Введите {i + 1} элемент множества: ")]

    return list1


n = verification_int("Введите кол-во элементов первого множества: ")
m = verification_int("Введите кол-во элементов второго множества: ")

print("Создание первого множества чисел:")
firstSetOfNumbers = list_creation(n)
print("Создание второго множества чисел:")
secondSetOfNumbers = list_creation(m)

print("Первое множество чисел:", firstSetOfNumbers,
      "Второе множество чисел:", secondSetOfNumbers,
      "Числа что встречаются в обоих множествах:", sorted(set(firstSetOfNumbers) & set(secondSetOfNumbers)),
      sep="\n")
