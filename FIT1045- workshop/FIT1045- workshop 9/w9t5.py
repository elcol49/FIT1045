queue = []
boolean = True
while boolean:
    check = input("Is any order served: ")
    if check == "No":
        num = int(input("Please enter the order number: "))
        queue.append(num)
        print("The order list is: " + str(queue))
    elif check == "Yes":
        queue.pop(0)
        print("The order list is: " + str(queue))
        if queue == []:
            print("The order list is empty")
            boolean = False
        
