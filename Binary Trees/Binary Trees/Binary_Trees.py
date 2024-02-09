class Node:
    def __init__(self):
        self.item = None
        self.leftPointer = None
        self.rightPointer = None
    

def CreateTree():
    global myTree
    myTree = [Node() for i in range(9)]
    global rootPointer
    rootPointer = None
    global nextFreePointer
    nextFreePointer = 0
    for index in range(9):
        myTree[index].leftPointer=index+1
    myTree[8].leftPointer=None

   

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
                else:
                    leftBranch=False 
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

CreateTree()
for j in range(5):
    itemInsert=input("Enter item to insert: ")
    AddNode(itemInsert)

OutputTree()

def FindItem(ItemSearch):
    pass

