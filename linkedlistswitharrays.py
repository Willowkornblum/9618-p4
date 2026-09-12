
data= ['A','B','C','D','E']
nextptr = [1,4,3,-1,2]
def finditeminLL():
    head = 0
    found = False
    current = head 

    item = input("Please enter what you want to find.\n")


    while(current != -1) and (found == False):
        if (data[current]== item):
            found = True
        else:
            current = nextptr[current]
    if found:
        print ("found")
        print ("item was found at",current)
    else:
        print("not found")
finditeminLL()
finditeminLL()
