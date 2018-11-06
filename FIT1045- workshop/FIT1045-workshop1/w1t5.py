import random
bias = str(input('bias'))
for x in range(0,10,1):
    y = random.random()

    if y < float(bias):
        print('true')
    else:
        print('false')

        
                  






import random
for x in range(0,10,1):
    y = random.randint(0,1)

    if y ==1:
        print('true')
    else:
        print('false')
                  

import random
for x in range(0,10,1):
    y = random.random()

    if y < 0.5:
        print('true')
    else:
        print('false')

        
