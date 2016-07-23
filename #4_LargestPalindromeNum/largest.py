def checkPalindrom(n):
    text = str(n)
    if(text[::-1] == text):
        return True
    return False


def largestPolindrome(digit1,digit2):
    max = 0
    for a in range(10**digit1 - 1,10**(digit1-1) - 1,-1):
        for b in range(10**digit2- 1,10**(digit2-1) - 1,-1):
            product = a*b
            if(checkPalindrom(product) and product>max):
                max = product
    return max




print largestPolindrome(3,4)