list1 = []
count = 0

while count < 5:
    num = input("input numbers with space in between for the list 5 times ")
#since the input is a string, we need to use .split to turn it into a list

    num1 = num.split(' ')

    list1.append(num1)

    count += 1

print(list1)

#task 4 discussion not completed
"""
method 2

list2 = []

count2 = 0

while count2 < 5:
    x = list(input("input numbers for the list 5 times & press enter when done"))
    
    list2.append(x)
    count2 += 1

print(list2)"""
