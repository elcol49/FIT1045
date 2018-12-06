def denominations():
    denominations = input("Please enter denominations: ")
    denominationsList = []
    denominations = denominations.replace(" ","")
    denominations = denominations.split(',')
    for item in range(len(denominations)):
        denominationsList.append(int(denominations[item]))
    return denominationsList

def selectionSortPrice():
    L = denominations()
    for i in range(len(L)):
        posOfMin = i
        for j in range(i+1, len(L)):
            if L[posOfMin] > L[j]:
                posOfMin = j
        #swapping
        tmp = L[i]
        L[i] = L[posOfMin]
        L[posOfMin] = tmp
    return L


def greedy():
    L = []
    a = selectionSortPrice()
    changeAmount = int(input("Please enter the amount you want to change: "))
    i = len(a)
    count = 0
    countList = []
    denominationList = []
    while i > -1:
        if a[i-1] <= changeAmount:
            changeAmount -= a[i-1]
            count += 1
                    
        else:
            if count != 0:
                denominationList.append(str(a[i-1]) + 'x' + str(count))
            count = 0
            i -= 1

    print("The balance left: " + str(changeAmount))
    print("Your denominations: " + str(denominationList))    

greedy()

