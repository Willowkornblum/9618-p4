from _typeshed import TraceFunction
import collections
import random
array = random.sample((0,101),20)

def printarray (intarray):
    output = ""
    for item in intarray:
        output = output + str(item) + " "
        print (output)

def bubblesort(intarray):
    swap = True
    while (swap == True):
        swap = False
        for index in range (0, len(intarray)-1):
            if intarray[index] > intarray[index + 1]:
                temp = intarray[index]
                intarray[index] = intarray[index +1]
                intarray[index + 1] = temp
                swap = True 
    return intarray


    def main():
        printarray(intarray)
        bubbled = bubblesort(intarray)
        print ("sorted")
        printarray(bubbled)
    
    def recursivebinarysearch(self,intarray,lowerbound,upperbound,value):
        num = (intarray)
        lowerbound = 0
        upperbound = (len (intarray - 1))
        value = input("what number are you looking for?\n")
        flag = False 
        index = 0
        while (flag == False) and (upperbound != lowerbound):
            index = ((upperbound - lowerbound) / 2)
            if (value == intarray[index]):
                 #flag = True 
                 return index
            elif (value > intarray[index]):
               # lowerbound = index + 1
               return recursivebinarysearch(intarray,lowerbound,index - 1,value)
            elif (value < intarray[index]):
                #upperbound = index - 1
                return recursivebinarysearch(intarray,index + 1,upperbound,value)
       # if (flag == True):
         #   return index
        else:
            return -1 

        def main():
            tofind = int(input("please enter in the integerr you wish to find"))
            position = recursivebinarysearch(bubblesort,0,19,tofind)
            if (position == -1):
                print ("not found")
            else:
                print("found at",position)


