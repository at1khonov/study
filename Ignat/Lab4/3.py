import random as rnd

n = int(input("Введите число строк: "))
m = int(input("введите число столбцов: "))
k = int(input("Введите строку k: "))
l = int(input("Введите cтолбец l: "))
massiv = []
for i in range(n):
    row = [rnd.randint(-9, 9) for i in range(m)]
    for i in range(len(row)):
        row[i] = int(row[i])
    massiv.append(row)
    print(row, sep="\t")

for i in range(n):
    massiv[i].pop(l - 1)
massiv.pop(k - 1)
for i in range(len(massiv)):
    for j in range(len(massiv[i])):
        print(massiv[i][j], end='\t')
    print()
