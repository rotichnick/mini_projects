
def Stack():
    global Mystack
    Mystack=[None for index in range(0,10)]
    global  StackFull
    global Top, Base
    Base=0
    Top=-1
    StackFull=10
    print(Mystack)

def Push(item):
    global Top
    global Mystack
    if Top<StackFull-1:
        Top+=1
        Mystack[Top]=item
    else:
        print("Stack is full, cannot push")
    print(Mystack)

def Pop():  
     global Top, Base, item   
     if Top == Base -1:    
         print("Stack is empty,cannot pop") 
     else:    
         item = Mystack[Top]
         Mystack[Top] =None
         Top = Top -1
     print(item)
     print(Mystack)

def InitialiseList():
    global NullPointer, FreeListPointer, StartPointer,MyLinkedList, MyLinkedListPointers
    NullPointer=-1
    MyLinkedList=[None for index in range(10)]
    MyLinkedList[0]=120
    MyLinkedListPointers=[index+1 for index in range(10)]
    MyLinkedListPointers[9]=NullPointer
    StartPointer=0
    FreeListPointer=1
    #return MyLinkedList, MyLinkedListPointers

def InsertItem(NewItem):
    global NullPointer, FreeListPointer, StartPointer,MyLinkedList, MyLinkedListPointers
    
    if FreeListPointer!=NullPointer:
        NewNodeptr=FreeListPointer
        MyLinkedList[NewNodeptr]=NewItem
        FreeListPointer=MyLinkedListPointers[FreeListPointer]
        ThisNodeptr=StartPointer
        PreviousNodePtr=NullPointer
        while ThisNodeptr!=NullPointer and MyLinkedList[ThisNodeptr]<NewItem:
            PreviousNodePtr=ThisNodeptr
            ThisNodeptr=MyLinkedListPointers[ThisNodeptr]

        if PreviousNodePtr== StartPointer:
            MyLinkedListPointers[NewNodeptr]=StartPointer
            StartPointer=NewNodeptr
        else:
            MyLinkedListPointers[NewNodeptr]=MyLinkedListPointers[PreviousNodePtr]
            MyLinkedListPointers[PreviousNodePtr]=NewNodeptr
    print( MyLinkedList, MyLinkedListPointers, StartPointer, FreeListPointer)

#InitialiseList()
#for g in range(6):
#    i=int(input("Item to insert: "))
#    InsertItem(i)

def Stars(Numbers):
    for x in range(Numbers):
        
        print(str(x) + " "+ "*")


def Factorial(number):
    if number==0:
        answer=1
    else:
        answer=number*Factorial(number-1)

    return answer

from asyncore import write
import random
from threading import main_thread
from tkinter import N
def NumberGuessingGame():
    myFile= open("New.txt", mode="w")

    numtoguess=random.randint(0,15)
    count=0
    guesscorrect=False 
    name=input("Name: ")
    myFile.write(name +"\n")
    while not guesscorrect:
        guess=int(input("Input your guess: "))
        myFile.write("Guess " +str(guess)+"\n")
        if numtoguess==guess: 
            guesscorrect=True 
            print("Congratulations!!!")
        else:
            if guess > numtoguess:
                print("Enter a smaller number ")
            else:
                print("Enter a larger number ")
        count+=1
    print(f"you made {count} guesses ")
    myFile.close()
#NumberGuessingGame()


def Recursion(a,b):
    if a<100:
        return 1
    else:
        if a> b:
            return 5 + Recursion(a-1, b)
        else:
            return 10+Recursion(a-10, b)



def R(a,b):
    result=1
    while a>100:
        if a>b:
            result+=5
            a-=1
        else:
            result+=10
            a-=10
    return result 
    



def Multiplication():
    num1=float(input("Enter num1"))
    num2=int(input("Enter num2"))
    Result=num1*num2 
    return Result

def UnKnown(x,y):
    result=1
    while x !=y:
        if x<y:
            print(x+y)
            result=result*2
            x+=1
        else:
            print(x+y)
            result//=2
            x-=1
    return result

#x=UnKnown(15,10)
#print(x)


def OuputTimesTable(n):
    for count in range(1,11):
        Result=count*n 
        print(f"{count} X {n} = {Result}")

#OuputTimesTable(8)

def twodlist():
    dinner=["pizza","meat","hot dog","humbugger"]
    drinks=["soda","tea","coffee"]
    dessert=["cake", "ice-cream"]
    food=[dinner,drinks,dessert]
    return (food)

myfood=twodlist()
main_course=["beef-ugali","chicken-rice"]
myfood.append(main_course)
newfood=myfood[1]
newfood.sort()
print(newfood)
for x in range(len(myfood)):
    for y in range(len(myfood[x])):
        print(myfood[x][y])

