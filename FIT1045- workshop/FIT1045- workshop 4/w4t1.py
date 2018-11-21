string = input("please input a word ")
stringL = string.lower()
stringS = stringL.replace(" ", "")
stringP = stringS.replace(",","")
stringP2 = stringP.replace("?","")
stringP3 = stringP2.replace(".","")

'''[x:z:y] means it slices where x = start, z = end, y = step
website for explaination about [::] 
https://stackoverflow.com/questions/9027862/what-does-listxy-do'''

reverse = stringP3[::-1]
if stringP3 == reverse:
    print("yes")
else:
    print("no")
    
