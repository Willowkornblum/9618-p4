numbers = [1,2,3,4,5,6,7,8,9]
num = float (input("what number would you like?\n"))
flag = False 
upperbound = (len (numbers) - 1)
lowerbound = 0
index = 0 
while (flag == False) and (upperbound != lowerbound):
    index = ((upperbound + lowerbound) // 2 )
    if num == (numbers[index]):
        flag = True 
    elif num > (numbers[index]):
        lowerbound = index + 1 
    else:
        upperbound = index - 1
if flag:
    print ("we found your number")
else:
    print ("sorry couldnt find your number")

