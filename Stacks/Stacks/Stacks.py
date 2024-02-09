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
Stack()   
Push("Nick")
Push("Rotich")
Pop()
