total = 0
c = 1
import random
start = random.randint(0,5)
end = random.randint(0,5)

while c==1:
    if (start>end):
        end = random.randint(0,5)
    else:
        c = 100

for n in range (start, end+1):
    for j in range (start, n+1):
        total += (2*(n**2) + 4*j)

print (total)
        

correct = ('false')
line = str(input('what is your guess? \nenter quit to exit \n'))
total = str(total)
           

while correct == ('false'):
    if line == 'quit':
            print ('you quit')
            correct = ('true')
            break
    if line != total:
           print ('incorrect guess')
           line = str(input('what is your guess? '))
    elif line == total:
            print ('it\'s correct')
            break
    
