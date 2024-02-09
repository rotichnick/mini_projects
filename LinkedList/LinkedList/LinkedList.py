#CREATING A LINKED LIST: 
from pickle import FALSE
from typing import ItemsView


def CreateLinkedList():
    global StartPtr, FreePtr, LinkedItems, LinkedPointers 
    StartPtr=-1
    FreePtr=0
    LinkedItems=[None for index in range(10)]
    LinkedPointers=[i+1 for i in range(10)]
    LinkedPointers[9]=-1
    print(LinkedItems)
    print(LinkedPointers)
    print("Start Pointer: " +str(StartPtr))
    print("Free Pointer: " +str(FreePtr))
   

def Insertitem(Item):
    global StartPtr, FreePtr, linkedItems, LinkedPointers
    NullPtr=-1
    if FreePtr==NullPtr:
        print("Linked List is FULL!")
    else:
        Temp=StartPtr
        StartPtr=FreePtr
        FreePtr=LinkedPointers[FreePtr]
        LinkedItems[StartPtr]=Item 
        LinkedPointers[StartPtr]=Temp
    print(LinkedItems)
    print(LinkedPointers)
    print("Start Pointer: " +str(StartPtr))
    print("Free Pointer: " +str(FreePtr))



def Search(item):
     global StartPtr, FreePtr, linkedItems, LinkedPointers
     NullPtr=-1
     found=False 
     currentptr=StartPtr 
     while (currentptr!=NullPtr) and not found:
         if LinkedItems[currentptr]==item: 
             found=True 
         else:
             currentptr= LinkedPointers[currentptr]
     if found==False:
         print("Item not found in the linked List")
     return currentptr 

def DeleteItem(item):
     global StartPtr, FreePtr, linkedItems, LinkedPointers
     NullPtr=-1
     if StartPtr==NullPtr:
         print("Linked list is EMPTY")
     else:
         index=StartPtr
         while (LinkedItems[index]!=item) and (index!=NullPtr):
             Oldindex=index 
             index=LinkedPointers[index] 

         if index==NullPtr:
             print("Item to delete not found!")
         else:
             Temp=LinkedPointers[index] 
             LinkedPointers[index]=FreePtr
             FreePtr=index 
             LinkedPointers[Oldindex]=Temp

     print(LinkedItems)
     print(LinkedPointers)
     print("Start Pointer: " +str(StartPtr))
     print("Free Pointer: " +str(FreePtr))

CreateLinkedList()
for i in range(5):
    value=int(input("Value: "))
    Insertitem(value)
returnVal=Search(990)
print("Search item found at index: " +str(returnVal))

DeleteItem(60)



