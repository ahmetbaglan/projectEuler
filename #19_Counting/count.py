day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def dayInYear(n):
    if(n%100 != 0 and n%4 == 0):
        return 366
    return 365


def numOfDays(a,b):
    (d1,m1,y1) = a
    (d2,m2,y2) = b
    m1 -= 1
    m2 -= 1

    tot = 0
    for y in range(y1+1,y2):
        tot += dayInYear(y)

    for m in range(m1, 12):

        tot += day[m]

    for m in range(0, m2-1):
        tot+= day[m]

    tot += day[m1]-d1
    tot += d2

    return tot

out = 0
for m in range(1,13):
    for y in range(1901,2001):
        if(numOfDays((1,1,1901),(1,m,y)) % 7 == 5):
            out+=1
print out

