from typing import Type
class EventItem:
    def __init__ (self,EventName,Type,Difficulty):
        self.__Eventname = EventName #STRING
        self.__Type = Type #STRING
        self.__Difficulty = Difficulty #INTEGER


    def GetName(self):
        return (self.__Eventname)
    def GetDifficulty(self):
        return (self.__Difficulty)
    def GetEventType(self):
        return(self.__Type)

Group = []

Group.append (EventItem("bridge","jump",3))
Group.append (EventItem("water wade","swim",4))
Group.append (EventItem("100 mile run","run",5))
Group.append (EventItem("dridlock","drive",2))
Group.append (EventItem("wall on wall","jump",4))

class Character:
    def __init__ (self,CharName,jump,swim,run,drive):
         self.__CharName = CharName #STRING 
         self.__jump = jump # INTEGER
         self.__swim = swim #INTEGER
         self.__run = run #INTEGER 
         self.__drive = drive #INTEGER
    def GetName(self):
        return(self.__CharName)

    def CalculateScore (self,Type,Difficulty):
        if Type == "jump":
            skill = self.__jump
        elif Type == "swim":
            skill = self.__swim
        elif Type == "run":
            skill = self.__run
        else: 
            skill = self.__drive 
        if skill >= Difficulty: 
            chance = 100
        else:
            diff = Difficulty - skill 
            if diff == 1:
                chance = 80
            elif diff == 2:
                chance = 60
            elif diff == 3:
                chance = 40
            elif diff == 5:
                chance = 20
        return chance

Character1 = Character("Tarz",5,3,5,1)
Character2 = Character("Geni",2,2,3,4)

character1Points = 0
character2Points = 0
for Event in range (0,5):
    character1score = Character1.CalculateScore(Group[Event].GetEventType(),Group[Event].GetDifficulty())
    character2score = Character2.CalculateScore(Group[Event].GetEventType(),Group[Event].GetDifficulty())
    if (character1score > character2score):
        character1Points += 1
        print (Character1.GetName(),"has won this event")
    elif (character2score > character1score):
        character2Points += 1
        print (Character2.GetName(),"has won this event")
    else:
        print ("draw")
if (character1Points > character2Points):
    print (Character1.GetName(),"has won with",character1Points,"points")
elif (character2Points > character1Points):
    print (Character2.GetName(),"has won with",character2Points,"points")
else:
    print("total draw")
