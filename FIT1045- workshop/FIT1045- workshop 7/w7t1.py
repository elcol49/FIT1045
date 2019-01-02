
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

for i in range(len(newList)):
        for j in range(2):
            newList[i][j] = int(newList[i][j])

for i in range(len(newList)):
    num = newList[i][0]
    num2 = newList[i][1]
    outer[num][num2] = 1
    num = 0
    num2 = 0
print(outer)
