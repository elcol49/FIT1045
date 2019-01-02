n = int(input("please enter a number: "))
inner = [0]*n
outer = []
for i in range(n):
    outer.append(inner[:])

count = 0
newList = []
while count < n:
    Q = input("enter position of queen: ")
    newList.append(Q.split(" "))
    count += 1

A = [0]*n
for i in range(len(newList)):
        for j in range(2):
           c = 0
        A[int(newList[i][0])] = int(newList[i][1])

print(A)

def printListInTableFormat(L):
    for i in range(len(L)):
        outer[i][A[i]] = 1

    for i in range(len(outer)):
        print(*outer[i])      
    return outer

a = printListInTableFormat(A)

def checkSolution(outer, n):
    diagonal = diagonalSum(A)
    horizontalSum = 0
    verticalSum = 0
    if n < 4:
        return False

    elif n >= 4:
        for i in range(n):
            for j in range(n):
                horizontalSum += outer[i][j]
                verticalSum += outer[j][i]
            if horizontalSum == 1 and verticalSum == 1 and diagonal:
                c = 0
                horizontalSum = 0
                verticalSum = 0
                if c == 0 and i == n - 1:
                    return True
            else:
                return False
            
def diagonalSum(outer):
    v = [outer[i+1] - outer[i] for i in range(len(outer)-1)]
    if -1 in v or 1 in v: 
        return False
    else:
        return True
            
if checkSolution(a, n):
    print("This is a real solution to the problem")
else:
    print("This is not a real solution to the problem")






        
