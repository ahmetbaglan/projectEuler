currency = [1,2,5,10,20,50,100,200]
def pos3(n):
    ways = [0] * max(n,200)

    for coin in currency:
        ways[coin-1]+=1
        for i in range(len(ways)-coin):
            ways[i+coin] += ways[i]

    return str(ways[n-1])


print pos3(200)
