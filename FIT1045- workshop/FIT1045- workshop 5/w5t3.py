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
selectionSortPrice(x)
fileOpen.close()
