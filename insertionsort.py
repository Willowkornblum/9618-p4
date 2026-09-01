Num = [3,6,8,5,4]

for i in range(1, len(Num)):
    key = Num[i]
    j = i - 1

    while (j >= 0) and (Num[j] < key):
        Num[j + 1] = Num[j]  
        j = j - 1
    Num[j + 1] = key 
print (Num)
