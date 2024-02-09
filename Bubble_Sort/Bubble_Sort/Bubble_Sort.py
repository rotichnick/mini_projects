
MyList=[109,19,5,23,9]

Last = len(MyList)
swap = False
arrlen = len(MyList)

n = len(MyList)-1
for i in range(len(MyList)- 1):
    for j in range(n):
        if MyList[j] > MyList[j + 1]:
            MyList[j], MyList[j + 1] = MyList[j + 1], MyList[j]
n=n-1

for x in MyList:
    print(x)









