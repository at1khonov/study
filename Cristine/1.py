import random as rnd

k = int(input("Введите количество столбцов: "))  # Задание пользователем количества столбцов
n = int(input("Введите количество строк: "))  # Задание пользователем количества строк
A = int(input('Введите А: '))
B = int(input('Введите B: '))
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
sum=0
counter=0
for i in range(n):
    for j in range(k):
        if A <= mass[i][j] <= B:
            sum=sum+mass[i][j]
            counter=counter+1
print("Сумма элементов попадающих под условие = ", sum)
print('Количество элементов = ', counter)
