#make a push procedure and a pop function for a stack
stack = [None for index in range(10)]
topPointer = -1 
basePointer = 0
item = None

def pop(): 
    global topPointer, basePointer , item 
    if (topPointer == basePointer - 1):
        print("stack is empty nothing to pop")
    else: 
        item = stack[topPointer]
        topPointer = topPointer - 1 
        message = "you've deleted", item
        print (message)


def push():
    global topPointer
    if (topPointer == len(stack) - 1):
        print("stack is full cant push")
    else:
        newvalue = input("Please enter value to add to stack:\n")
        topPointer = topPointer + 1 
        stack[topPointer] = newvalue 
        print (newvalue, "has been pushed")

push ()
push ()
push()
pop()
push()
pop()




