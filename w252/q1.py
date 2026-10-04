
class Bird: 
    def __init__(self,Species,DistancePerHour):
        self.__Species = Species                                            #STRING
        self.__DistancePerHour = DistancePerHour                            #REAL
        self.__XPosition = 500.0                                            #REAL
        self.__YPosition = 500.0                                            #REAL


    def GetSpecies(self):
        return self.__Species

    def GetPosition(self):
        toreturn = "x =",str(self.__XPosition),"y =",str(self.__YPosition)
        return toreturn


    def Move(self,Direction,min):
        if (Direction == 'N'):
            self.__YPosition = self.__YPosition + ((self.__DistancePerHour/60)*min)
        elif (Direction == 'S'):
            self.__YPosition = self.__YPosition - ((self.__DistancePerHour/60)*min)
        elif (Direction == 'E'):
            self.__XPosition = self.__XPosition +  ((self.__DistancePerHour/60)*min)
        elif (Direction == 'W'):
            self.__XPosition = self.__XPosition - ((self.__DistancePerHour/60)*min)

Bird1 = Bird("cockatiel",71.0)
Bird2 = Bird("macow",56.0)



tomove = 0
print ("1 is\n", Bird1.GetSpecies(),"at\n",Bird1.GetPosition(),"\n","2 is\n",Bird2.GetSpecies() ,"at\n",Bird2.GetPosition())
tomove = int(input("whould you like to move bird 1 or 2\n"))
temps = tomove
while (tomove > 0) and (tomove < 3):
    direction = input ("should the bird move N S E or W\n")
    if (direction == 'N'):
        tomove = 3
    elif (direction == 'S'):
        tomove = 3
    elif (direction == 'E'):
        tomove = 3
    elif (direction == 'W'):
        tomove = 3
    else:
        print("must imput directing as N,S,E or W")
        tomove = 0 
while (tomove == 3):
    minfly = int(input("pleas enter the time the bird will fly ot the nearest minute in the range of 0-500\n"))
    if (minfly >= 0 ) and (minfly <= 500):
        while (temps == 1):
            if (direction == "N"):
                Bird1.Move("N",minfly)
            elif (direction == "E"):
                Bird1.Move("E",minfly)
            elif (direction == "S"):
                Bird1.Move("S",minfly)
            elif (direction == "W"):
                Bird1.Move("W",minfly)
            temps = 0
        while (temps == 2):
            if (direction == "N"):
                Bird2.Move("N",minfly)
            elif (direction == "E"):
                Bird2.Move("E",minfly)
            elif (direction == "S"):
                Bird2.Move("S",minfly)
            elif (direction == "W"):
                Bird2.Move("W",minfly)
            temps = 0
    tomove = 4

print ("bird one is", Bird1.GetSpecies(),"and is at", Bird1.GetPosition())
print ("bird two is", Bird2.GetSpecies(),"and is at", Bird2.GetPosition())
