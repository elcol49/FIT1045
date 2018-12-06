fileName = input('enter file name: ')
fileOpen = open(fileName, 'r')

def openF(file):
    aList = []
    for line in file:
        line = line.split("\n")
        line = line.pop(0)
        line = line.split(",")
        line[0] = int(line[0])
        line[1] = float(line[1])
        aList.append(line)
    return aList
    
def printList(L):
    for i in range(len(L)):
        print(str(L[i][0]) + ' kms, $' + str(L[i][1]))

def selectionSortDistance(L):
    for i in range(len(L)):
        posOfMin = i
        for j in range(i+1, len(L)):
            if L[posOfMin][0] > L[j][0]:
                posOfMin = j
        #swapping
        tmp = L[i]
        L[i] = L[posOfMin]
        L[posOfMin] = tmp

    printList(L)

def selectionSortPrice(L):
    for i in range(len(L)):
        mini = i
        for j in range(i+1, len(L)):
            if L[mini][1] > L[j][1]:
                mini = j
        #swapping
        temp = L[mini]
        L[mini] = L[i]
        L[i] = temp

    printList(L)  


x = openF(fileOpen)
while True:
    inputt = input('enter choice: print, sort dist, sort price or quit ')
    if inputt == 'print':
        printList(x)
    if inputt == 'sort dist':
        selectionSortDistance(x)    
    if inputt == 'sort price':
        selectionSortPrice(x)
    if inputt == 'quit':
        print('you quit the program')
        break

fileOpen.close()
