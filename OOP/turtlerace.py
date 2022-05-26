from turtle import Turtle

laura = Turtle()
laura.color("red")
laura.shape("turtle")
laura.penup()
laura.goto(100, -160)
laura.pendown()

rik = Turtle()
rik.color("blue")
rik.shape("turtle")
rik.penup()
rik.goto(100, -140)
rik.pendown()

lauren = Turtle()
lauren.color("pink")
lauren.shape("circle")
lauren.penup()
lauren.goto(100, -120)
lauren.pendown()


carrieanne = Turtle()
carrieanne.color("green")
carrieanne.shape("arrow")
carrieanne.penup()
carrieanne.goto(100, -100)
carrieanne.pendown()
from random import randint

for movement in range(500):
    laura.forward(randint(1,5))
    rik.forward(randint(1,6))
    lauren.forward(randint(1,7))
    carrieanne.forward(randint(1,8))
