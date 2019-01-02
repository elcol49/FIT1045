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
            if int(newList[i][0]) not in A:
                A.insert(int(newList[i][1]),int(newList[i][0]))
print(A)
