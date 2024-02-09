MyList = [23, 45, 65, 25, 67, 87, 99, 48]
UpperBound = 7
Lowerbound = 0

print("Please enter the number to search:")
item = int(input())

found = False
index = Lowerbound

while not found and index <= UpperBound:
    if item == MyList[index]:
        found = True
    else:
         index += 1

          

if found:
    print("Item found at index: " + str(index))
else:
    print("Item not found in the list")
