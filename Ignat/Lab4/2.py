import random as rnd
n = int(input('Введите количество строк '))
m = int(input('Введите количество столбцов '))
massiv = [] * n
for i in range(n):
    row = [rnd.randint(-3,9) for i in range(m)]
    for i in range(len(row)):
        row[i] = int(row[i])
    massiv.append(row)
    print(row)
for i  in range(n):
    minimum=0
    for j in range(len(massiv[i])):
        if massiv[i][j]<minimum:
            print(i+1,'\t',j+1)
            break
print()
for i in range(len(massiv)):
    minimum=0
    for j in range(len(massiv[i])):
        if massiv[j][i]<minimum:
            print(j+1,'\t',i+1)
            break
