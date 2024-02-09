import pickle


class CarRecord:
    def __init__(self):
        self.vehicleID=0
        self.registration=""
        self.enginesize=0
def hash(key):
    key=int(key)
    address=(key%10)+50
    return address 

mycar=[0,0]
mycar=[CarRecord() for i in range(2)]
carfile=open("Carfile.txt", mode="+bw")
for i in range(2):
    mycar[i].vehicleID=input("Enter vehicle id")
    mycar[i].registration=input("enter registration")
    mycar[i].enginesize=input("Enter engine size")
    address=hash(mycar[i].vehicleID)
    carfile.seek(address)
    pickle.dump(mycar[i],carfile)
carfile.close()

print(mycar)

