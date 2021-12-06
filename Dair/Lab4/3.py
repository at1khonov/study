import random as rnd

k = int(input("Введите количество столбцов: "))  # Задание пользователем количества столбцов
n = int(input("Введите количество строк: "))  # Задание пользователем количества строк
k1 = int(input('Введите k1: '))
k2 = int(input('Введите k2: '))
mass = []  # Объявление пустого списка массива
row = []  # Объявление пустого списка строки
for i in range(n):  # Цикл для заполнения массива случайными значениям
    for i in range(k):
        row.append(rnd.randint(-40, 30))
    mass.append(row)
    row = []
for i in range(n):  # Цикл для вывода исходного массива
    for j in range(k):
        print(mass[i][j], end=' ')
    print()
