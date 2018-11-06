import math

x = float(input('value of x: '))
n = float(input('value of n: '))

log = math.log(x)
power = log/n

a = math.exp(power)
print('The ' + str(n) + 'th root is ' + str(a))
