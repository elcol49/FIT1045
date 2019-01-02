openBracket = ['(', '[', '{']
closeBracket = [')', ']', '}']

userIn = input("Enter string of brackets: ")

newList = []
for char in userIn:
    newList.append(char)

n = 0
mid = len(newList) // 2
if len(newList) % 2 == 0:
    while n < mid:
        push = newList.pop(0)
        if push in openBracket:
            close = newList.pop()
            if close in closeBracket:
                if push == '[' and close == ']':
                    a = True
                elif push == '{' and close == '}':
                    a = True
                elif push == '(' and close == ')':
                    a = True
                else:
                    a = False
            else:
                a = False
        else:
            a = False
        n += 1
else:
    a = False

if a:
    print("Output: YES")
else:
    print("Output: NO")

'''
stack = []
n = 0
mid = len(newList) // 2
if len(newList) % 2 == 0:
    while n < mid:
        if newList[n] in openBracket:
            stack.append(newList[n])
            close = newList.pop()
            if close in closeBracket:
                if newList[n] == '[' and close == ']':
                    a = True
                elif newList[n] == '{' and close == '}':
                    a = True
                elif newList[n] == '(' and close == ')':
                    a = True
                else:
                    a = False
            else:
                a = False
        else:
            a = False
        n += 1
else:
    a = False

if a:
    print("Output: YES")
else:
    print("Output: NO")
'''
