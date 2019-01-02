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

A = []
for i in range(len(newList)):
        for j in range(2):
            c = 0
        A.insert(int(newList[i][1]),int(newList[i][0]))
print(A)

def printListInTableFormat(L):
    for i in range(len(L)):
        outer[A[i]][i] = 1

    for i in range(len(outer)):
        print(*outer[i])

printListInTableFormat(A)
