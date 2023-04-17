"""
Задача №15. 
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза

Input: 
    5 -> 5 1 6 5 9
Output: 
    1 9
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
 
countWatermelon = VerificationInt("Введите количество арбузов: ")
watermelon = []

for i in range(countWatermelon):
    watermelon += [VerificationInt(f"Введите вес {i+1} арбуза: ")]

print(f"\n Вам нужно взять: {watermelon.index(max(watermelon))+1} арбуз" +
      f"\n Вашей тёщи нужно взять: {watermelon.index(min(watermelon))+1} арбуз")