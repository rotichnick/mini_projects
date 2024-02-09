#Q-TWo

class Card:
    #Number as integer
    #Colour as string
    def __init__(self, num, col):
        self.__Number=num 
        self.__Colour=col 
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour


#Main Program:
print("\n \n")
print("Start of Q2:")
MyFile=open("CardValues.txt", mode="r")
CardArr=[]
for f in range(30):
    
    number=MyFile.readline()
    #print(f"Number: {num_ber}")
    Color=MyFile.readline().strip()
    #print(f"Colour: {Color}")
    CardArr.append(Card(number,Color))
    
MyFile.close()
    
#for x in range(30):
#    print(CardArr[x].GetNumber2())
#    print(CardArr[x].GetColour2())
global Cardinit
Cardinit=[False for x in range(30)]
def ChooseCard():
    choice=int(input("Enter a number: "))
    while choice<1 or choice>30:
        choice=int(input("Wrong! Enter a number again: "))
    found=False 
    
    while not found :
        if Cardinit[choice-1]==False: 
            found=True 
            Cardinit[choice-1]=True
        else:
            print(f"Card number {choice} is already taken")
            choice+=1
        
    return choice-1
#playerscores=open("Playerscores.txt",mode="w")

#for player in range(1,5):
#    for playerchoice in range(1,4):
#        x=ChooseCard()
#        print(f"Player {player} choice {playerchoice} chose: {x} ") 
#        playerscores.write(f"Player {player} choice {playerchoice} chose: {x} ")
#playerscores.close()
player1=[None for x in range(10)] 
for playerchoice in range(1,5):
    x=ChooseCard()
    x1=CardArr[x].GetNumber()
    x2=CardArr[x].GetColour()
    
    player1[playerchoice]=Card(x1,x2)
for x in range(1,5):
    print(f"The Number is: {player1[x].GetNumber2()}" )
    print(f"The colour is: {player1[x].GetColour2()}" )
                                 



















