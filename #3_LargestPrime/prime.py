
def m(n):
    k = n
    d ={}
    index = 1
    max = 2
    while k>2:
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
    return max

print m(600851475143)






