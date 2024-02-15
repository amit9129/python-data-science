from turtle import *
speed(3)
def square():
    for i in range (4):
        forward(100)
        right(90)

def hexgon():
    for i in range(6):
        forward(100)
        right(60)

for i in range(6):
    fd(100)
    square()
    rt(60)




hideturtle()
mainloop()
