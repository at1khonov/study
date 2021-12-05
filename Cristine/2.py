import random as rnd
n = int(input("Введите количество элементов: "))
mass = []
for i in range(n):
    mass.append(rnd.randint(-100, 100))
summ=0
for i in range(4):
    summ=mass[i]+summ
print(summ)
