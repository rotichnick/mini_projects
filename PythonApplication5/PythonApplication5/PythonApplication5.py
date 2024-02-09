import turtle
shelly=turtle.Turtle()
shelly.begin_fill()
shelly.color("red")
for n in range(36):
    for i in range(6):
        shelly.forward(100)
        shelly.left(60)
    
    shelly.right(10)



input("Press any key to continue..")


