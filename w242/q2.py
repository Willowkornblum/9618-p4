
class Queue :
    def __init__ (self): 
        self.HeadPointer = -1               #INTEGER
        self.TailPointer = 0                #INTEGER
        self.QueueArray = []
        for i in range (100):
            self.QueueArray.append(-1)

TheQueue = Queue()
def enqueue(TheQueue,TheData):
    if (TheQueue.HeadPointer == -1):
        TheQueue.QueueArray[ TheQueue.TailPointer] = TheData
        TheQueue.HeadPointer = 0 
        TheQueue.TailPointer += 1
        return 1
    else:
        if (TheQueue.TailPointer > 99):
            return -1
        else:
            TheQueue.QueueArray[TheQueue.TailPointer] = TheData
            TheQueue.TailPointer += 1 
            return 1 
def ReturnAllData(TheQueue):
    if (TheQueue.HeadPointer == -1):
        i = 0
    else:
        i = TheQueue.HeadPointer
    alldata = ""
    while (i != TheQueue.TailPointer):
        alldata = alldata +' '+ str(TheQueue.QueueArray[i])
        i += 1
    return alldata
     
print("you are about to enter 10 integers >= 0 \n")
i = 0
queuefull = False 
while (( i < 10) and (queuefull == False)):
    value = int(input("please enter an integer above 0: \n"))

    if (value >= 0):
        outputfromenqueue = enqueue(TheQueue,value)
        if (outputfromenqueue == -1):
            queuefull = True 
            print ("the queue is full")
        else:
            print("item has been added")
            i += 1

finaloutput = ReturnAllData(TheQueue)
print (finaloutput)

def Dequeue (TheQueue):
    if (TheQueue.HeadPointer == -1):
        return -1
    else:
        todeq = TheQueue.QueueArray[TheQueue.HeadPointer]
        TheQueue.HeadPointer = TheQueue.HeadPointer + 1 
        return todeq
  
i = 0 
empty = False
while (i < 2) and ( empty == False):
    result = Dequeue(TheQueue) 
    if (result == -1):
        print("queue epty")
        empty = True
    else: 
        i += 1
updates = ReturnAllData(TheQueue)
print (updates)



