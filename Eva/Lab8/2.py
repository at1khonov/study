def null(x):
    if x[0] == 0:
        return int(x[1])
    else:
        return int(x)


file = open('date.txt', 'r+')
maxday = 0
maxmonth = 0
maxyear = 0
result = ""
for line in file:
    if maxyear < int(line[6:11]):
        maxyear = int(line[6:11])
        result = line
    elif maxyear == int(line[6:11]):
        if maxmonth < null(line[3:5]):
            maxmonth = null(line[3:5])
            result = line
        elif maxmonth == null(line[3:5]):
            if maxday < null(line[0:2]):
                result = line
                maxday = null(line[0:2])
file.close()
print(result)
