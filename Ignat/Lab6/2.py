from math import sqrt
import random as rnd


def distance(x1, y1, x2, y2):
    dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return dist


n = int(input("Введите количество строк: "))  # Задание пользователем количества строк
mass = []
row = []  # Объявление пустого списка строки
for i in range(n):  # Цикл для заполнения массива случайными значениям
    for i in range(2):
        row.append(rnd.randint(-40, 30))
    mass.append(row)
    row = []

for i in range(n):  # Цикл для вывода исходного массива
    for j in range(2):
        print(mass[i][j], end=' ')
    print()
max=0
for i in range(n):
    for j in range(n):
        l=int(distance(mass[i][0], mass[i][1], mass[j][0], mass[i][1]))
        if max < l:
            max = l
print(max)
