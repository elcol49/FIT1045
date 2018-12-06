numCupcakes = int(input("please enter the number of cupcakes: "))
rCal = input("respective calorie counts of each cupcake: ")

rCal = rCal.split(" ")
rCalc = []
for i in rCal:
    i = int(i)
    rCalc.append(i)

def selectionSort(L):
    for i in range(len(L)):
        posOfMin = i
        for j in range(i+1, len(L)):
            if L[posOfMin] < L[j]:
                posOfMin = j
        #swapping
        tmp = L[i]
        L[i] = L[posOfMin]
        L[posOfMin] = tmp

    return L
    
total = 0

for i in range(numCupcakes):
    a = selectionSort(rCalc)
    total += 2**i * a[i]
    
print(total)
