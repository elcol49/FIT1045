fileName = input('enter file name: ')
fileOpen = open(fileName, 'r')

def open(file):
    aList = []
    for line in file:
        line = line.split("\n")
        line = line.pop(0)
        line = line.split(",")
        line[0] = int(line[0])
        line[1] = float(line[1])
        aList.append(line)
    printList(aList)
    
def printList(x):
    for i in range(len(x)):
        print(str(x[i][0]) + ' kms, $' + str(x[i][1]))

open(fileOpen)

fileOpen.close()
