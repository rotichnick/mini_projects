print("Text Files")
try:
    MyFile=open("Students.txt",mode="r")

    Students=[]
    LineRead=MyFile.readline()
    Students.append(LineRead)
    while LineRead !="":
        LineRead=MyFile.readline()
        print(LineRead)
        Students.append(LineRead)

    MyFile.close()
except :
    print("Invalid file name")





