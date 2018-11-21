file = open('palindromic.txt','r')

for i in file:

    string = i
    stringS = string.replace(" ", "")
    stringL = stringS.lower()
    stringS = stringL.replace(" ", "")
    stringP = stringS.replace(",","")
    stringP2 = stringP.replace("?","")
    stringP3 = stringP2.replace(".","")
    stringP4 = stringP3.replace("\n","")

    reverse = stringP4[::-1]
    
    if stringP4 == reverse:
        print(stringP4 + " yes")
    else:
        print(stringP4 + " no")

file.close()














        
