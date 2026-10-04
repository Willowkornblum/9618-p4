treearray = []
for i in range (0,50):
    treearray.append(-1,-1,-1)      #dont really get this 
rootpointer = -1
freenode = 0 

def addnode():
    index = 0
    flag = False
    toadd = int(input("please enter the integer you woud like to add"))
    while (index < 50) and (flag == False):
        if (rootpointer == -1):
            rootpointer = toadd 
            flag = True
        elif (rootpointer > toadd):
            rootpointer.left = rootpointer
            return addnode(rootpointer,toadd)
        elif (rootpointer < toadd):
            rootpointer.right = rootpointer 
            return addnode(rootpointer,toadd)
    print("the tree is full")


