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


#add times for same day in the list
listTime = []
listTableTime = []

for i in range(z):
    if table[i][0] == table[i+1][0]:
        listTime.append(table[i][1])
    else:
        listTime.append(table[i][1])
        listTableTime.append(listTime)
        listTime = []

#separate 3 feb saturday 
listSaturdayTime = []        
for i in range(y-3,y):
    listSaturdayTime.append(table[i][1])
listTableTime.append(listSaturdayTime) #all the tide values in an inner list that's in a table


#to find for the lowest/smallest value
lowestList = []
lowestTime = []

for i in range(len(listTableTide)):
    
    lowest = listTableTide[0][0]
    for j in range(len(listTableTide[i])):
        
        if lowest > listTableTide[i][j]:
            lowest = listTableTide[i][j]
            lowesti = i
            lowestj = j
            lowestT = listTableTime[lowesti][lowestj] #to find for the lowest time at lowesti & lowestj
            
    lowestList.append(lowest)
    lowestTime.append(lowestT)


#to find for the highest/biggest value
highestList = []
highestTime = []
    
for i in range(len(listTableTide)):
    
    highest = listTableTide[0][0]
    for j in range(len(listTableTide[i])):
        
        if highest < listTableTide[i][j]:
            highest = listTableTide[i][j]
            highesti = i
            highestj = j
            highestT = listTableTime[highesti][highestj] #to find for the highest time at highesti & highestj
            
    highestList.append(highest)
    highestTime.append(highestT)

#store the days along with lowest and highest tidal values & lowest and highest time
fullList = []
for i in range(len(listDays)):
    bigList = [listDays[i]] + [lowestTime[i]] + [lowestList[i]] + [highestTime[i]] + [highestList[i]]
    fullList.append(bigList)
    print(bigList)

#average time for lowest
lowestTotal = 0

for i in range(len(lowestTime)):
    lowestTotal += lowestTime[i]

averageLowest = round(lowestTotal/i, 2)


#average time for highest
highestTotal = 0

for i in range(len(highestTime)):
    highestTotal += highestTime[i]

averageHighest = round(highestTotal/i, 2)


print('Over the full period, on average the lowest and highest tides occurred at ' + str(averageLowest) + ' and ' + str(averageHighest) + ' hours after midnight')









        
