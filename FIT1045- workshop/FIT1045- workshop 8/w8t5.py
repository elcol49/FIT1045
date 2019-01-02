n = int(input("Input a positive integer n "))

def printToN(n):
    if n != 1:
        printToN(n-1)
    print(n)

print("Output of printToN ")
printToN(n)

def printSquares(n):
    if n != 1:
        printSquares(n-1)
    print(n**2)

print("Output of printSquares ")
printSquares(n)

def sumOfSquares(n):
    if n == 0:
        return 0
    else:
        return n*n + sumOfSquares(n-1)

print("Output of sumOfSquares ")
print(sumOfSquares(n))
