total = 0
start = int(input('starting value: '))
end = int(input('end value: '))
divisible_value = int(input('divisible value: '))
                           
for n in range (start, end+1):
    if n % divisible_value == 0:
        total += 2*(n**2) + 4*n

print (total)

