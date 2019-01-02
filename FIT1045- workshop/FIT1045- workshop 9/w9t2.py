n = int(input("Please enter a positive integer n "))

L = []
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def printL(n):
    for i in range(1, n+1):
        L.append(factorial(i))
    print(L)

printL(n)
