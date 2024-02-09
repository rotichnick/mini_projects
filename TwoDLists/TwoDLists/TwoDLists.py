from numbers import Number


global Jobs 
global Numberofjobs
Numberofjobs=0
Jobs=[]
def Initialise():
    for row in range(10):
        Jobs.append([-1,-1])

def Addjob(jobnumber, priority):
    global Numberofjobs
    if Numberofjobs==0:
        Numberofjobs+=1
        Jobs[0][0]=jobnumber 
        Jobs[0][1]=priority 
    else:
        index=Numberofjobs 
        Jobs[index][0]=jobnumber 
        Jobs[index][1]=priority 
        Numberofjobs+=1
Initialise()
for x in range(3):
 Addjob(3,0)

print(Jobs)
print(Numberofjobs)



