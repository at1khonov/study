def nod(x, y):
    if y == 0:
        return x
    else:
        return nod(y, x % y)


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
num = nod(x, y)
print("Наибольший общий делитель двух чисел: ", num)
