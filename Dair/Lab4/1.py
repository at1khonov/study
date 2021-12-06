import random as rnd
n = int(input("Введите количество элементов: "))
A = int(input("Введите A: "))
B = int(input("Введите B: "))
mass = []
for i in range(n):
    mass.append(rnd.randint(-100, 100))
summ=0
for i in range(n):
    if A<mass[i]<B:
        summ=summ+mass[i]
print("Сумма элементов= ", summ)
