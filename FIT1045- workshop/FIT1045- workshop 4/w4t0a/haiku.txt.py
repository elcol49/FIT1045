
stringList = []
smallList = []

file = open('mod_haiku.txt','r') #opens the file for idle to read
outfile = open('haiku.txt','w') #creates the file to save txt

for i in file:

    y = i.split("\t") #split sentences joined with tabs
    stringList = y #assign to list

    stringList = "\n".join(stringList) #add new lines with join function

    for j in stringList: 

        x = j.split(";") #split words joined with ;
        smallList = x #add words to the smallList

        space = (" ".join(smallList)) #add space between words
        result = str(space) #if dont convert to string then it'll return boolean for \n separators
        print(result)
        
        outfile.write(result)

outfile.close() #must be out of loop. if not, it'll close if it's in the loop

file.close()
        



    


        
        




        
