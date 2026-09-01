#Queue = [None for smt in range(0,3)]

Queue = [None] * 3

#for smt in range (0,3): 
   # Queue [smt] = None

QueueLength = 0
QueueFull = len(Queue)
FrontPointer = 0 
RearPointer = -1 

# enqueue 

def enqueue ():
    global RearPointer, QueueLength
    if (QueueLength < QueueFull):
        inputchar = input ("Please enter what youd like to add to queue:\n") 
        if (RearPointer == QueueFull-1):
            RearPointer = 0
        else:      
            RearPointer += 1 
        Queue[RearPointer] = inputchar 
        QueueLength += 1 
    else:
        print("queue is completly full")
    print (Queue)
#dequeue
def dequeue():
    global FrontPointer,QueueLength
    if (QueueLength > 0):
        item = Queue[FrontPointer]
        Queue[FrontPointer] = None 
        if (FrontPointer == QueueFull-1):
            FrontPointer = 0 
        else:
            FrontPointer += 1
        QueueLength -= 1 
        print( item, " was deleted.")
    else:
        print("queue is empty")
    print (Queue)

enqueue()
enqueue()
dequeue()
enqueue()
enqueue()
dequeue()
enqueue()
enqueue()
dequeue()
enqueue()
enqueue()
dequeue()
dequeue()
dequeue()
dequeue()
