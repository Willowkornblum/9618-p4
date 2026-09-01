class employee:
    def __init__ (self,name,staffno,height):
        self.__name = name
        self.__staffno = staffno
        self.__height = height
    def growup(self,growthspurt):
        self.__height += growthspurt
    def showDetails(self):
        print("employee Name" , self.__name)
        print("employee number", self.__staffno)
        print("emplyees height is",self.__height,"cm")
#overloading: 
    def onboarding (self,startdate = None):
        if (startdate != None):
            print ("you are an employee at our company starting from", startdate)
        else:
            print("you are an employee at our company")


# emp1= employee("willow kornblum", 33,170)
# emp1.showDetails()
# emp1.growup(5)
# emp1.showDetails()
# emp2 = employee("abdullah",65,180)
# emp2.showDetails()
# emp2.growup(5)
# emp2.showDetails()

class parttime(employee):
    def __init__(self,name,staffno,height):
        employee.__init__(self,name,staffno,height)
        self.__fulltimestaff = False 
        self.__hoursworked = 0
        self.__hourlysalary = 5
    def showDetails(self):
        employee.showDetails(self)
        print("hoursworked:",self.__hoursworked )
    def gethoursworked (self):
        return(self.__hoursworked)
    def salaryincrease (self):
        self.__hourlysalary *= 1.1

class fulltime(employee):
    def __init__(self,name,staffno,height):
        employee.__init__(self,name,staffno,height)
        self.__fulltimestaff = True
        self.__yearlysalary = 1000
    def showDetails(self):
        employee.showDetails(self)
        print("yearlysalary is:", self.__yearlysalary)
    def getyearlysalary (self):
        return(self.__yearlysalary)
    def salaryincrease (self):
        self.__yearlysalary *= 1.1 #self.__yearlysalary += ((self.__yearlysalary/100) *10)


emp1 = fulltime("willow k",45,170)
emp1.showDetails()
emp2= parttime("abdullah",28,180)
emp2.showDetails()
#overloading
emp1.onboarding()
emp1.onboarding("28th of september")
emp1.showDetails()
emp1.salaryincrease()
emp1.showDetails()