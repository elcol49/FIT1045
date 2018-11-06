import random
bias = float(input('bias'))
num = int(input('number of times: '))
heads = 0
tails = 0
body = 0

for x in range(0,num,1):
    y = random.randrange(3)

    if y == 1:
        print('heads')
        heads += 1
    elif y == 2:
        print('tails')
        tails += 1
    else:
        print('body')
        body += 1

ratio = heads/num
print (ratio)
print(heads, tails, body)

        
                  






