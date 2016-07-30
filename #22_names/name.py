
f = open('p022_names.txt','r')

text = f.read()
text = text.replace('"','')
names = text.split(",")
names = sorted(names)
import string
alph = list(string.ascii_uppercase)

def getAlphValue(a):
    global alph
    sum = 0
    for i in a:
        sum+=alph.index(i)+1
    return sum
def getRank(a):
    global names
    return  names.index(a)+1

def getAll(a):
    return getAlphValue(a)*getRank(a)

sum = 0
for i in names:
    sum+=getAll(i)

print sum