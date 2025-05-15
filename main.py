import turtle
import time
from random import randint
from time import sleep
#Screen Part
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("lightblue")
turtle_screen.setup(width=600, height=600)
turtle_screen.title("CatchTheTurtle")

#Turtle Object Part
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("green")
myTurtle.shapesize(3)


#Score Part
score = 0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 350)
score_writer.color("blue")
score_writer.write(f"Skorunuz : {score}", align="center", font=("Arial", 24, "normal"))

#Timer Part
timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(0, 310)
sure = 20


def clickchangescore(x,y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Skorunuz : {score}", align="center", font=("Arial", 24, "normal"))
    

def stopmoving(x,y):
    myTurtle.home()

def kalan_sure():
    global sure
    for i in range(sure, -1, -1):
        timer_writer.clear()
        timer_writer.write(f"Kalan süre : {i}", align="center", font=("Arial", 24, "normal"))
        myTurtle.penup()
        myTurtle.teleport(randint(-250, 250), randint(-250, 250))
        time.sleep(1)
        if i == 0:
            timer_writer.clear()
            timer_writer.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
            myTurtle.onclick(stopmoving)
            break

score_writer.write(f"Skorunuz : {score}", align="center", font=("Arial", 24, "normal"))
myTurtle.onclick(clickchangescore)
kalan_sure()

turtle_screen.mainloop()




