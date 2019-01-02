fileOpen = open("small.txt", 'r')

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
print(outer)
                  
        
