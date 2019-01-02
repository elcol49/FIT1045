fileOpen = open("small2.txt", 'r')

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

# returns the index of target if target is found, otherwise returns -1
def binarySearch2(aList, target, low, high):
    mid = (low + high)//2
    # return target if it is found
    if aList[mid][1] == target:
        print("Post code is " + str(aList[mid][0]))
        return aList[mid][0]
    # if the range has only one element, return -1 because if this element was the target it would have been returned by above if block
    if low == high:
        return -1
    # otherwise, recursively search in the smaller range
    if aList[mid][1] > target:
        return binarySearch2(aList,target,low,mid-1)
    else:
        return binarySearch2(aList,target,mid+1,high)

target = input("Please enter suburb name: ")
binarySearch2(outer,target,0,len(outer))
