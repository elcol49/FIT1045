openFile = open('tidal.txt', 'r')
tidalList = []
table = []
count = 0

for item in openFile:
    
    item = item.split('\n') #convert to list that contains ['string','']
    item = item.pop(0) #remove element in index 0 from list so it's just 'string'
    item = item.split(' meters') #convert to list that contains ['string', ' meters']
    item = item.pop(0) #remove first element in index 0 from list
    tidalList = item.split(',') #puts it in a list ['string','string','string']
    tidalList[1] = float(tidalList[1]) #convert string in index 1 to float
    tidalList[2] = float(tidalList[2]) #convert string in index 2 to float
    table.append(tidalList)

print(table)

    
openFile.close()

    

        

        





     
