d =  {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
      12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eightteen',19:'nineteen',
      20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred', 1000:'thousand'}

def getToTex(n):
    andOk = False
    out = ''
    if(n/100>0):
        out = out + d[n/100] + d[100]
        n = n%100
        andOk = True
    if(n/10 > 0):
        if(andOk):
            out += "and"
            andOk = False
        else:
            andOk = True
        if(n>=20):
            out = out + d[(n/10)*10]
            n = n%10
        else:
            out = out + d[n]
            n = 0

    if(n>0):
        if(andOk):
            out+='and'

        out = out + d[n]

    return  out


def till(k):
    top = 0
    for n in range(k+1):
        t = getToTex(n)
        top += len(t)
        print t,n
    return top

print till(1000)
# print getToTex(29)
# print len(getToTex(115))