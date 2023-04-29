import math
from turtle import *

title("Never Give Up Project")

def zemer(k):
    return 15*math.sin(k)**3

def zemer_dyshi(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(0)
bgcolor("black")

penup()
goto(-220, 250)
color("white")
write("Never Give Up", font=("Arial", 20, "bold"))
goto(-150, 180)
#write("OOO Kujdestare", font=("Arial", 12, "normal"))
goto(0, 0)
pendown()

for zeemeer in range(6000):
    goto(zemer(zeemeer)*20,zemer_dyshi(zeemeer)*20)
    for i in range(5):
        color("red")
    goto(0, 0)

done()
