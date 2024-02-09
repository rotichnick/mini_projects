global currentsize
currentsize=0
global contacts
global sorted_contacts
contacts=[]
sorted_contacts=[]
def menu():
    print("OPTIONS")
    print("1 to enter contact details, 2 to display all contact details")
    print("3 to delete all contact details and 0 to exit the program")
    choice=int(input("input choice"))
    while choice!=1 and choice!=2 and choice!=3:
        choice=int(input("input choice again 0,1,2 or 3"))
    return choice

def contactinput():
    global sorted_contacts
    currentsize=0
    newcontact=[]
    numofcontacts=int(input("How many contacts would you like to insert? "))
    while numofcontacts<=0 or numofcontacts>5:
        numofcontacts=int(input("You can only insert 5 or less contacts? "))
    currentsize+=numofcontacts
    if currentsize<100:
        for index in range(numofcontacts):
            name=input("enter last name and first name: ")
            telephone=input("enter your tel number: ")
            newcontact=[name,telephone] 
            contacts.append(newcontact)
    else:
        print("Array is full")

    if currentsize>=2:
        sorted_contacts = sorted(contacts, key=lambda x: x[0])

def displaycontacts():
    
    print("This section works!")

def deletecontacts():
    delete=input("Are you sure you want to delete the items? Y to delete, N to preserve").capitalize()
    count=0
    if delete=="Y":
        for i in range(len(contacts)):
            for l in range(0,2):
                contacts[i][l]=None 
             
            count+=1
        print(f"{count} contacts were deleted!")
    else:
        print("Items preserved:")
   
    

selection=menu()
while selection!=0:
    if selection==1:
        contactinput()
    elif selection==2:
        displaycontacts()
    elif selection==3:
        deletecontacts()
    selection=menu()




