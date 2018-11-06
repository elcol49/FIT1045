total = 0
total2 = 0
start = int(input('starting value: '))
end = int(input('end value: '))

for n in range (start, end+1):
    for j in range (start, n+1):
        total += (2*(n**2) + 4*j)
        
print (total)
