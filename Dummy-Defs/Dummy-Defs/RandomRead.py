import pickle
def hash(key):
    key=int(key)
    address=(key%10)+50
    return address 
VehicleID=int(input("ID"))
CarFile = open('Carfile.txt','rb+')  # open file for binary read 
Address = hash(VehicleID)
CarFile.seek(Address)
ThisCar = pickle.load(CarFile.VehicleID)  # load record from file 
print(ThisCar)
CarFile.close()
