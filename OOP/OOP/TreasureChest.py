class TreasureChest:
    def __init__(self,q,a,p):
        self.__question=q
        self.__answer=a
        self.__points=p
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, ans):
        if ans==int(self.__answer):
            return True
        else:
            return False
    def getPoints(self, attempts):
        if attempts==1:
            return int(self.__points)
        elif attempts==2:
            return int(self.__points)//2
        elif attempts==3 or attempts==4:
            return int(self.__points)//4
        else:
            return 0
        
TreasureChestArr=[]
def readData():
    
        MyF=open("TreasureChestData.txt",mode="r")
        for x in range(15):
                 ques=MyF.readline().strip()
                 ans=MyF.readline().strip()
                 pts=MyF.readline().strip()
                 TreasureChestArr.append(TreasureChest(ques,ans,pts))

readData()

num=int(input("Enter number between 1 and 5"))
print(f"What is: {TreasureChestArr[num-1].getQuestion()}")

correct=False 
count=1
while not correct:
    answer=int(input("Your answer? "))
    if TreasureChestArr[num-1].checkAnswer(answer):
        correct=True
    else:
        count+=1
        print("Attempt again! ")
pointsawarded=TreasureChestArr[num-1].getPoints(count)
print(pointsawarded)