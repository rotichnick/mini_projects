class Dog:
    species="Cannines"
    def __init__(self, name, age):
            self.name=name 
            self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#dog1=Dog("Myles", 12)
#print(dog1)
#dog2=Dog("Buddy", 13)

#print(dog2.speak("Woo Woo"))



#print(dog2)

class Car:
    def __init__(self, color, mileage):
        self.color=color 
        self.mileage=mileage 
    def describe(self):
        return f"The {self.color} has {self.mileage} Miles"

class Node:
    def __init__(self):
        self.__item = None
        self.leftPointer = None
        self.rightPointer = None
    def printer(self):
        print(f"{self.__item} and {self.leftPointer} and {self.rightPointer}")

def CreateTree():
    global myTree
    myTree=Node()
    myTree.__item="i"
    myTree.printer()
   
#CreateTree()

def AddNode(newItem):
    global rootPointer
    global nextFreePointer
    if nextFreePointer is None:
        print("Tree is full, no nodes free")
    else:
        #use next free node.
        itemAddPointer=nextFreePointer
        nextFreePointer=myTree[nextFreePointer].leftPointer
        itemPointer=rootPointer
        #check for empty tree
        if itemPointer is None:
            rootPointer=itemAddPointer
        else:
            #find where to insert a new leaf
            while (itemPointer is not None):
                oldPointer=itemPointer
                if myTree[itemPointer].item>newItem:
                    #choose left subtree
                    leftBranch=True 
                    itemPointer=myTree[itemPointer].rightPointer
            if leftBranch: #use left or right branch
                myTree[oldPointer].leftPointer=itemAddPointer
            else:
                myTree[oldPointer].rightPointer=itemAddPointer
    #store the item to be added in the new node
    myTree[itemAddPointer].leftPointer=None 
    myTree[itemAddPointer].rightPointer=None 
    myTree[itemAddPointer].item=newItem

def OutputTree():
    for i in range(9):
        print(f"LEFT POINTER: {myTree[i].leftPointer} ITEM: {myTree[i].item} RIGHT POINTER: {myTree[i].rightPointer}")
    print(f"ROOT POINTER {rootPointer} FREE POINTER: {nextFreePointer}" )

#CreateTree()
#AddNode(24)
#AddNode(13)
#OutputTree()


class Vehicle:
    #construtor
    def __init__(self, id, e):
        #instance attributes
       self.__VehicleID=id 
       self.__EngineSize=e 
       self.__DateofReg=None
       self.__PrchasePrice=0.00
       self.__Registration=""
    def SetDateofRegistration(self, dor):
        self.__DateofReg=dor
    def SetPurchasePrice(self, pp):
        self.__PrchasePrice=pp 
    def SetRegistration(self, r):
        self.__Registration=r 
    
    def PrintDetails(self):
        print(f"The vehicle whose ID is {self.__VehicleID} has engine size of {self.__EngineSize} ")
    def GetDateofReg(self):
        return f"The Registration ID is : {self.__DateofReg} " 
    def GetPurchasePrice(self):
        return f"The Purchase price is : {self.__PrchasePrice} "
    def GetRegistration(self):
        return f"The vehicle ID is  {self.__Registration} " 
    
#sub class definition
class PsvCar(Vehicle):
    #constructor of the sub class
    def __init__(self, id, e, sit):
        Vehicle.__init__(self, id, e)#statement calls constructor of base class
        self.__sitting_pass=sit
        
        self.__standing_pass=0
            #setter for the sub class
    def setStandingPass(self, stand):
        self.__standing_pass=stand 
        #getters for the sub class
    def PrintDetails(self):
        print("Vehicle Details")
        Vehicle.PrintDetails(self)
        print(f"The vehicle has a sitting capacity of: {self.__sitting_pass} and {self.__standing_pass} standing passengers")
    
#myPsv_Car=PsvCar("HP-111", 2500, 36)
#myPsv_Car.setStandingPass(14)

#myPsv_Car.PrintDetails()

#print(myPsv_Car.GetPurchasePrice())
#print(myPsv_Car.GetEngineSize())

#Try to access private attributes


#privatec=PrivateCar("PQ-98-12", 2300)
#privatec.setCapacity(5)
#print(privatec.GetPurchasePrice())

#Test the built in classes.
#Q-One
class Card:
    #Attribute declaration as comments
    #1
    #2
    def __init__(self, Num, Col):
        self.__Number=Num 
        self.__Colour=Col 

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
class Hand:
    def __init__(self, cd1, cd2, cd3, cd4, cd5):

        self.__Cards=[] 
        self.__Cards.append(cd1)
        self.__Cards.append(cd2) 
        self.__Cards.append(cd3)
        self.__Cards.append(cd4)
        self.__Cards.append(cd5)
        self.__FirstCard=0
        self.__NumberCards=5
    def GetCard(self,index):
        return self.__Cards[index]

def CalculateValue(Player):
    score=0
    for count in range(0,5):
        CardGot=Player.GetCard(count)
        #print(f"Card Got is: {CardGot}")
        score+=CardGot.GetNumber()
        Colour=CardGot.GetColour()
        if Colour=="red":
            score+=5
        elif Colour=="blue":
            score+=10
        else:
            score+=15
    return score

#Creating card instances
OneRed=Card(1,"red") 
TwoRed=Card(2,"red")
ThreeRed=Card(3,"red")
FourRed=Card(4,"red")
FiveRed=Card(5,"red")
OneBlue=Card(1,"blue")
TwoBlue=Card(2,"blue")
ThreeBlue=Card(3,"blue")
FourBlue=Card(4,"blue")
FiveBlue=Card(5,"blue")
OneYellow=Card(1,"yellow")
TwoYellow=Card(2,"yellow")
ThreeYellow=Card(3,"yellow")
FourYellow=Card(4,"yellow")
FiveYellow=Card(5,"yellow")

#Creating hand instances with card objects:
Player1=Hand(FiveYellow, FiveBlue,ThreeRed,TwoYellow,OneYellow)

Player2=Hand(FiveBlue, ThreeBlue,FourYellow,FiveYellow,OneYellow)
x=Player1.GetCard(0)
print(x.GetColour())
print(x)
Player1_Score= CalculateValue(Player1) 
Player2_Score= CalculateValue(Player2) 

if Player1_Score>Player2_Score:
    print(f"Player one won with {Player1_Score} Points")
elif Player2_Score> Player1_Score:
    print(f"Player two won with {Player2_Score} Points")
else:
    print(f"Game was a draw")

