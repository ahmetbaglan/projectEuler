
k = [1]
m = 1
for i in range(3,1003,2):
    m += i - 1
    for f in range(4):
        k.append(m + f*(i-1))
    m = m +f*(i-1)

sum = 0

for i in k:
    sum += i

print sum