
MyList=[1,3,5,6,9,10,12,14,16,19,20,23,45,56,78]

found=False

SearchFailed=False
MaxItems=len(MyList)
print(MaxItems)
First=0
Last=MaxItems-1
searchitem=int(input("Enter item to search: "))
while (not found) and (not SearchFailed):
    middle=(First+Last)//2
    if MyList[middle]==searchitem:
        found=True
    else:
         if First>=Last:
             SearchFailed=True
         else:
             if MyList[middle]>searchitem:
                 last=middle-1
             else:
                 First=middle+1

if found:
    print("Item found at index" +str(middle))
else:
    print("Item not found.")






