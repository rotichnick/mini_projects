
def WriteToFile():

    MyFile = open ("MyText.txt","w")
    
    TextLine = input("Please enter a line of text ")
    MyFile.write(TextLine)
    MyFile.close


def ReadFromFile():
    print("The file contains this line of text")
    MyFile = open ("MyText.txt","r")
    TextLine = MyFile.read()
    print(TextLine)
    MyFile.close()


#program to get the product of two numbers:

#number1=int(input("Please enter number 1: "))
#print("\n")
#print("\n")

#number2=int(input("Please enter the second number: "))
#print("\n")
#print("\n")

#product=number1*number2

#print(str(number1) +" X " +str(number2) +" is " +str(product))
#print("\n")
#print("\n")

Mylist=[16,5,48,96,9,18,31,20]

found=False 
index=-1
maxindex=7

item=int(input("Enter Item to search: "))
while index<maxindex and not found:
    index=index+1
    if Mylist[index]==item:
        found=True 

if found: 
    print('Item found at index: ' +str(index))
else:
    print("Item not found: ")