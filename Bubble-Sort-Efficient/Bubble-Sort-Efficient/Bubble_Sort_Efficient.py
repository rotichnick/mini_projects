
MyList=[12,9,0,6,2]

n=len(MyList)
Swap=True

while Swap:
    Swap=False
    for index in range(n-1):
        if MyList[index]>MyList[index+1]:
            MyList[index],MyList[index+1]=MyList[index+1], MyList[index]
            Swap=True
    n=n-1

for i in MyList:
    print(i)