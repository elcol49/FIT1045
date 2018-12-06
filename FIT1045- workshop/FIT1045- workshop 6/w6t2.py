fileOpen = open('items.txt','r')

capacityInput = input("Please enter the capacity of the knapsack: ")
capacity = capacityInput
capacity.replace(" ", "")
capacity = int(capacity)

newLine = []
for line in fileOpen:
    line = line.split('\n')
    if "" in line:
        line.remove("")
    string = line.pop()
    string = string.split("kg $")
    newLine.append(string)

inner = []
outer = []
for i in newLine:
    for j in i:
        j = int(j)
        inner.append(j)
    outer.append(inner)
    inner = []
print(outer)       

#least weight
def selectionSort(L):
    for i in range(len(L)):
        posOfMin = i
        for j in range(i+1, len(L)):
            if L[posOfMin][0] > L[j][0]:
                posOfMin = j
        #swapping
        tmp = L[i]
        L[i] = L[posOfMin]
        L[posOfMin] = tmp
    return L

a = selectionSort(outer[:])
for i in range(len(outer)):
    if a[i][0] <= capacity:
        capacity -= a[i][0]
        for j in range(len(a)):
            if a[i][1] == outer[j][1]:       
                print("item " + str(j) + " value= " + str(a[i][1]) + "$")
    
