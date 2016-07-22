def multiples(elements, r):
    total = 0
    for i in range(r+1):
        for e in elements:
            if( i % e == 0):
                print i
                total += i
                break
    return total

print multiples([3,5],99)