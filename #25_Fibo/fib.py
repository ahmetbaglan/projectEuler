from eulerLib import *

maxLoop = 10**5
def sumIt(l):
    out = ''
    for j in topla(l):
        out+=str(j)
    return out


def fibNor(digit):
    onetwo = ['1','1']
    new = '0'
    for i in range(2,maxLoop):
        new = sumIt(onetwo)
        onetwo=[onetwo[1],new]
        if(len(new)>=digit):
            return i+1
    return 1



print fibNor(2)
