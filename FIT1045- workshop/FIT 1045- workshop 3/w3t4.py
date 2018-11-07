#method 1- according to question

list2 = [0]*5

for i in range(5):
    x = input("please enter numbers with space: ")
    y = x.split(' ')
    list2[i] = [0]*len(y)

    for j in range(len(y)):
        #int- to change from string to int
        #y[j] means element in list y index j
        list2[i][j] = int(y[j])
        
print(list2)    

#method 2- using append method
list1 = []
count = 0

while count < 5:
    num = input("input numbers with space in between for the list 5 times ")
#since the input is a string, we need to use .split to turn it into a list

    num1 = num.split(' ')

    list1.append(num1)

    count += 1

print(list1)


#method 3- using list(input()) but if input 1111 it means 1,1,1,1 so cannot input
#numbers like 13 because it'll be shown as 1,3

list2 = []

count2 = 0

while count2 < 5:
    x = list(input("input numbers for the list 5 times & press enter when done"))
    
    list2.append(x)
    count2 += 1

print(list2)

