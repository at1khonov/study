import random as rnd

N = int(input('Введите количество чисел: '))
K = int(input('Введите кратное: '))
file = open('random.txt', 'w+')
file2 = open('result.txt', 'w+')
for i in range(N):
    file.write(str(rnd.randint(-100, 100)) + '\n')
file.close()
file = open('random.txt', 'r+')
for line in file:
    if int(line) % K == 0:
        file2.write(line)
file.close()
file2.close()
