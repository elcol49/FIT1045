n = int(input("please enter a number: "))
inner = [0]*n
outer = []
for i in range(n):
    outer.append(inner)

rightd = 0
for i in range(len(outer)):
    for j in range(i):
        rightd += outer[i][j]
print(rightd)

leftd = 0
for i in range(len(outer) - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        leftd += outer[i][j]
print(leftd)

subtraction = rightd - leftd
