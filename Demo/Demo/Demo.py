#Product of two number

def Product(num1, num2):
    #num1=int(input("Enter Number 1: "))
    #num2=float(input("Enter Number 2: "))
    prod=num1*num2
    print("The product of 2 numbers is: " +str(prod))


def ProdFunction(num1, num2):
    
    Result=num1*num2
    return Result

def InitialiseArray():
    MyList=[0 for index in range(10)]
    print(MyList)


global Top, StackFull, MyStack

def CreateStack():
    global Top, StackFull, MyStack
    MyStack=[0 for x in range(10)]
    StackFull=len(MyStack)-1
    Top=-1


def Push(Item):
    global Top, StackFull, MyStack
    if Top==StackFull:
        print("Stack is Full, cannot push item")
    else:
        Top+=1
        MyStack[Top]= Item

def Pop():
    global Top, StackFull, MyStack
    if Top==-1:
        print("Stack is empty! ")
    else:
        CopyItem=MyStack[Top]
        print(CopyItem)
        Top=Top-1

def CreateQueue():
    global Front,Rear, QueueFull,NumberInQueue, Max, MyQueue
    MyQueue=[0 for x in range(10)]
    Max=len(MyQueue)
    QueueFull=Max- 1
    Front=-1
    Rear=-1
    NumberInQueue=0
    print(MyQueue)

def Enqueue(NewItem):
     global Front, Rear, QueueFull,NumberInQueue, MyQueue, Max
     if Front==-1:
         Front=0

     if NumberInQueue== Max:
         print("Queue is FULL")
     elif Rear==QueueFull:
         Rear=0
     else:
         Rear=Rear+1
     MyQueue[Rear]=NewItem
     NumberInQueue=NumberInQueue+1
     print(MyQueue)
     print("Rear: " +str(Rear), "Front: " +str(Front))



def DeQueue():
     global Front, Rear, QueueFull,NumberInQueue, MyQueue, Max
     if NumberInQueue==0:
         print("Queue is EMPTY! ")
     else:
         CopyItem=MyQueue[Front]
         print(CopyItem)
         NumberInQueue-=1
     if Front==QueueFull:
         Front=0
     else:
         Front+=1
     print("MyQueue after DeQueue: " +str(MyQueue) +" Front: ")
     print(Front)


#CreateQueue()
for i in range(4):
   item=int(input("Enter: "))
   Enqueue(item)
#DeQueue()

a=12
x=a%2
print(x)