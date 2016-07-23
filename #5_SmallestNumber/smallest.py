
def m(n):
    k = n
    d ={}
    index = 1
    max = 2
    while k>=2:
        index+=1
        if(k % index == 0):
            if(index in d.keys()):
                d[index]+=1
            else:
                d[index] = 1
            if(index>max):
                max = index
            k = k/index
            index = 1
    return d

def find(number):
    outDict = {}
    for n in range(number):
        nowDict = m(n)
        for k in nowDict.keys():
            if( k in outDict):
                if(nowDict[k]>outDict[k]):
                    outDict[k] = nowDict[k]
            else:
                outDict[k] = nowDict[k]
    total = 1
    for n in outDict.keys():
        for times in range(outDict[n]):
            total*=n

    return total


print find(20)
