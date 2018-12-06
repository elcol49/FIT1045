# this function is to print the element in the index from 0 - n
def printElements(alist):
    for i in range(len(alist)):
        print("At index " + str(i) + " is the element " + str(alist[i]))

#get the index for the smallest number while the loop is running
def getMinIndex(alist, start, stop):
    miniIndex = start
    for i in range(start+1, stop):
        if alist[i] < alist[miniIndex]:
            miniIndex = i
    return miniIndex

#swap the position between the smallest and i
def swapNum(alist,i,j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

#selection sort
def selectionSort(alist):
    n = len(alist)

    for k in range(n):
        min_position = getMinIndex(alist, k, n)
        swapNum(alist, k, min_position)

#this func joins selectionSort and printElements func
def printAscending(alist):
    selectionSort(alist)
    copy = alist[:]
    printElements(copy)

alist = [9, 7, 5, 3]
printAscending(alist)

