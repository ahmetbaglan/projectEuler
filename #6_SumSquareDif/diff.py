

def sumOfSquaresTill(n):
    return (n * (n+1) * (2*n + 1) )/6


def squareOfSum(n):
    return ((n * (n+1))/2)**2

def diff(n):
    return squareOfSum(n)-sumOfSquaresTill(n)

print diff(100)