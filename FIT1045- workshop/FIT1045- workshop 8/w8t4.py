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

def binarySearch1(L, string):
    low = 0 
    high = len(L)-1
         # continue until range is not empty
    while low <= high:
        mid = (low + high) // 2
            # return the index if target is found
        if L[mid][1] == string:
            print("Post code is " + str(L[mid][0]))
            return (L[mid][0])
            # otherwise update the range
        elif L[mid][1] > string:
            high = mid-1
        else:
            low = mid+1
      # if range is empty and target is not found, return -1
    return -1  

userInput = input("Enter suburb name: ")    
binarySearch1(outer, userInput)
