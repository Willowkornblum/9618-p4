sample = [5,8,9,4,3,7,1]
upperbound = len(sample)-1 
swap = True 
while (swap) and (upperbound > 0):
    swap = False 
    for index in range (upperbound):
        if (sample[index] > sample[index + 1]):
            temp = sample[index]
            sample[index] = sample[index + 1]
            sample[index + 1]  = temp 
            swap = True 
    upperbound = upperbound - 1 
print ("this is the right order: \n",sample)


