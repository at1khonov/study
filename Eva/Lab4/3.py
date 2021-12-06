import random as rnd

k = int(input("Введите количество столбцов: "))  # Задание пользователем количества столбцов
n = int(input("Введите количество строк: "))  # Задание пользователем количества строк

mass = []  # Объявление пустого списка массива
row = []  # Объявление пустого списка строки
for i in range(n):  # Цикл для заполнения массива случайными значениям
    for i in range(k):
        row.append(rnd.randint(-5, 20))
    mass.append(row)
    row = []

for i in range(n):  # Цикл для вывода исходного массива
    for j in range(k):
        print(mass[i][j], end=' ')
    print()

mass1 = set()  # Создаем пустые множества для записи в них значений индексов столбцов и строк с отрицательными элементами
mass2 = set()  # такие "костыли" нужны чтоб не было повторяющихся записей в дальнейшем списке

for i in range(
        n):  # Находим индексы строк и столбцов, содержащих отрицательные элементы и записываем их в ранее созданные множества
    for j in range(k):
        if mass[i][j] < 0:
            mass1.add(i)
            mass2.add(j)

mass1 = list(mass1)  # Конвертируем множества в списки для дальнейшей работы с ними
mass2 = list(mass2)

for i in range(len(mass1) - 1, -1, -1):  # Удаляем строки
    mass.pop(mass1[i])

for i in range(len(mass)):  # удаляем столбцы
    for j in range(len(mass2) - 1, -1, -1):
        mass[i].pop(mass2[j])

print()

for i in range(len(mass)):  # Цикл для вывода получившегося массива
    for j in range(len(mass[i])):
        print(mass[i][j], end=' ')
    print()
