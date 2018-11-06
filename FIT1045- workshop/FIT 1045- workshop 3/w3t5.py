diceRoll = 0
listNum = []

import random
#this is to generate random numbers from 1 -> 6 like in a dice
numOnDice = random.randrange(1,6)

while diceRoll < 1000:
    #adds numOnDice into the list
    listNum.append(numOnDice)
    
    #adds the numbers in the list together
    total = sum(listNum)
    diceRoll += 1

    mean = total/diceRoll

print(mean)
    
