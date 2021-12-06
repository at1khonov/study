import random as rnd
n = int(input("Введите количество элементов: "))
mass = []
for i in range(n):
    mass.append(rnd.randint(-100, 100))
summ=0
proizvedeniye=1
for i in range(4):
    summ=mass[i]+summ
    proizvedeniye=mass[i]*proizvedeniye
print("Сумма=", summ)
print("Произведение=", proizvedeniye)
