class Picture:
    def __init__(self, desc, w, h, fc):
        self.__Description=desc 
        self.__Width=w 
        self.__Height=h 
        self.__FrameColour=fc 
    def GetDescription(self):
        return self.__Description 
    def GetHeight(self):
        return self.__Height 
    def GetWidth(self):
        return self.__Width 
    def GetColour(self):
        return self.__FrameColour 
    def setDescription(self, description):
        self.__Description=description 
global PicArray
PicArray=[]

def ReadData():
    count=0
    try:
        f=open("Pictures.txt", mode="r")
        for x in range(21):
            d=f.readline().strip()
            w=int(f.readline())
            h=int(f.readline())
            c=f.readline().strip()
            #print(f"description: {d} Colour: {c} width {w} height: {h}")
            PicArray.append(Picture(d,w,h,c))
            count+=1
    except :
        print("Invalid file name")
    f.close()
    return count, PicArray

#Main program:
total,PicArray=ReadData()
print(total)
col=input("Enter colur").lower()
maxh=int(input("Enter height"))
maxw=int(input("Enter width"))
for i in range(total):
    if PicArray[i].GetColour() == col and PicArray[i].GetHeight() <= maxh and PicArray[i].GetWidth() <= maxw:
        print(f"Pic description: {PicArray[i].GetDescription()} Width: {PicArray[i].GetWidth()} and height: {PicArray[i].GetHeight()}")