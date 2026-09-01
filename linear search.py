# linear searching emotions
#create arry
emotions = ["happy","sad","angry","sleepy","relaxed","scared"]
#input
feeling = input("what are you feeling?\n")
#set up flag 
found = False 
index = 0
while (found == False) and (index < len(emotions)):
    if (feeling == emotions[index]):
        found = True 
    index += 1
if (found == True):
    print("i know what youre feeling")
else:
    print ("i dont know what youre feeling")  
"""happy days 
sad days 
long days"""