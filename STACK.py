data = list([])
while True:
    print("Select Operation to perfom on the stack ")
    print("ADD = add to the stack"+"\n"+"POP =remove element from the stack"+"\n"+"EXIT = Exit program")
    operation = str(input())
    while True:
        if operation == "ADD":
            add_stack  = input("what do you want to add to the stack?")
            if len(add_stack) !=0:
                data.append(add_stack)
                print(data)
                input("press something to proced")
                break
            else:
                print("The Operation is empy")
        if operation == "POP":
            if len(data) >0:
                data.pop()
                print(data)
                input("press something to proced")
                break

            else:
                print("Stack is empty")
        if operation =="EXIT":
            exit()



