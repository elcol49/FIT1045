'''a_list = []

count = 0
while count < 5:
    a_list[count] = count
    count = count + 1

print(a_list)'''

# line 5 list assignment index out of range
# a_list[0] = count whereby it means element in index 0 = count but since it is
# an empty list, there's no element with index 0. hence, there's an error

a_list = [1, 2, 3, 4, 5]

count = 0
while count < 5:
    a_list[count] = count #replace index number count with int count
    count = count + 1

print(a_list)
