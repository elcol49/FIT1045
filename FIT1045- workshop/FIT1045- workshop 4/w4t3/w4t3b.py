openFile = open('tidal.txt', 'r')
tidalList = []
table = []

for item in openFile:
    
    item = item.split('\n') #convert to list that contains ['string','']
    item = item.pop(0) #remove element in index 0 from list so it's just 'string'
    item = item.split(' meters') #convert to list that contains ['string', ' meters']
    item = item.pop(0) #remove first element in index 0 from list
    tidalList = item.split(',') #puts it in a list ['string','string','string']
    tidalList[1] = float(tidalList[1]) #convert string in index 1 to flaot
    tidalList[2] = float(tidalList[2]) #convert string in index 2 to float
    table.append(tidalList)

print(table)

openFile.close()

y = len(table)
z = y-2
x = range(y)
listTide = []
listTableTide = []
listDays = []

#this is until friday 2 feb. if not, it'll show error: list out of range
for i in range(z):
    if table[i][0] == table[i+1][0]:
        listTide.append(table[i][2])
    else:
        listTide.append(table[i][2])
        listTableTide.append(listTide)
        listDays.append(table[i][0])
        listTide = [] #returns empty list so that other elements will be appended into an empty list each time

#separate 3 feb saturday 
listSaturday = []        
for i in range(y-3,y):
    listSaturday.append(table[i][2])
listTableTide.append(listSaturday) #all the tide values in an inner list that's in a table
    
listDays.append(table[y-1][0]) #all the days in a list


#to find for the lowest/smallest value
lowestList = []

for i in range(len(listTableTide)):
    
    lowest = listTableTide[0][0]
    for j in range(len(listTableTide[i])):
        
        if lowest > listTableTide[i][j]:
            lowest = listTableTide[i][j]
            
    lowestList.append(lowest)


#to find for the highest/biggest value
highestList = []    
    
for i in range(len(listTableTide)):
    
    highest = listTableTide[0][0]
    for j in range(len(listTableTide[i])):
        
        if highest < listTableTide[i][j]:
            highest = listTableTide[i][j]
            
    highestList.append(highest)

#store the days along with lowest and highest tidal values
fullList = []
for i in range(len(listDays)):
    bigList = [listDays[i]] + [lowestList[i]] + [highestList[i]]
    fullList.append(bigList)

#prints the result of the day and the lowest & highest tides                        
for i in range(len(listDays)):
    print(str(fullList[i][0]) + ': ' + str(fullList[i][1]) + ' meters at lowest, ' + str(fullList[i][2]) + ' meters at highest')


    
