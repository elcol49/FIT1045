fileName = input("Enter name of postcode file: ")
fileOpen = open(fileName, 'r')

newList = []
for line in fileOpen:
    L1 = line.strip().split('\t')
    L1[1] = L1[1].split(',')
    newList.append(L1)

inner = []
outer = []
for i in range(len(newList)):
    for j in range(len(newList[i][1])):
        inner.append(int(newList[i][0]))
        inner.append(newList[i][1][j])
        outer.append(inner)
        inner = []

for i in range(len(outer)):
    posOfMin = i
    for j in range(i+1, len(outer)):
        if outer[posOfMin][1] > outer[j][1]:
            posOfMin = j
    #swapping
    tmp = outer[i]
    outer[i] = outer[posOfMin]
    outer[posOfMin] = tmp
    
for i in range(len(outer)):
    print(outer[i][0],outer[i][1],sep=" ")
    


