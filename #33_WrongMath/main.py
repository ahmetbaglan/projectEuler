import eulerLib as e
outList = []

for nom in range(10,100):
    for denom in range(nom,100):
        realVal = float(nom)/denom

        if(nom == denom):
            continue

        d = str(denom)
        n = str(nom)

        for i in d:
            if(i=='0'):
                continue
            if i in n:
                newN = n.replace(i,'')
                newD = d.replace(i,'')
                try:
                    if((float(newN)/int(newD))==realVal):
                        outList.append((nom,denom))

                except:
                    pass


out = (1,1)
for i in outList:
    nom = i[0]
    denom = i[1]
    out = (out[0]*nom, out[1]*denom)

nom = e.carpanlaraAyir(out[0])
denom = e.carpanlaraAyir(out[1])

for i in nom:
    if i in denom:
        k = min(nom[i], denom[i])
        nom[i] = nom[i]-k
        denom[i] = denom[i]-k

a = 1
b = 1
for i in nom:
    a*= i**(nom[i])
for i in denom:
    b*=i**(denom[i])

print "The nominator is ",a
print "The denominator is ",b



