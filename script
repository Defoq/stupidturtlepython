import turtle
import random as rand
import os
import re
import json


screen = turtle.Screen()
screen.bgcolor("black")

player1 = turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.penup()
player1.goto(-300 , 200)
player1.pendown()

player2 = turtle.Turtle()
player2.color("red")
player2.shape("turtle")
player2.penup()
player2.goto(-300 , -200)
player2.pendown()

player3 = turtle.Turtle()
player3.color("orange")
player3.shape("turtle")
player3.penup()
player3.goto(-300 , -100)
player3.pendown()

player4 = turtle.Turtle()
player4.color("pink")
player4.shape("turtle")
player4.penup()
player4.goto(-300 , -300)
player4.pendown()

player5 = turtle.Turtle()
player5.color("springgreen")
player5.shape("turtle")
player5.penup()
player5.goto(-300 , 100)
player5.pendown()

player6 = turtle.Turtle()
player6.color("cyan")
player6.shape("turtle")
player6.penup()
player6.goto(-300 , 25)
player6.pendown()

linedrawer = turtle.Turtle()
linedrawer.hideturtle()
linedrawer.color("blue")
linedrawer.penup()
linedrawer.goto(300,-400)
linedrawer.pendown()
linedrawer.left(90)
linedrawer.forward(800)
linedrawer.write("Finish" , font=("consolas" , 25))

winannouncer = turtle.Turtle()
winannouncer.hideturtle()

for i in range(100):

    dice1 = rand.randrange(10,101)
    dice2 = rand.randrange(10,101)
    dice3 = rand.randrange(10,101)
    dice4 = rand.randrange(10,101)
    dice5 = rand.randrange(10,101)
    dice6 = rand.randrange(10,101)

    if player1.pos() >= (300 , -400):
        player1.penup()
        winannouncer.color("green")
        winannouncer.write("Green wins" , font=("consolas" , 15))
        break

    elif player2.pos() >= (300 , -400):
        player2.penup()
        winannouncer.color("red")
        winannouncer.write("Red wins" , font=("consolas" , 15))
        break

    elif player3.pos() >= (300 , -400):
        player3.penup()
        winannouncer.color("orange")
        winannouncer.write("Orange wins" , font=("consolas" , 15))
        break

    elif player4.pos() >= (300 , -400):
        player4.penup()
        winannouncer.color("pink")
        winannouncer.write("Pink wins" , font=("consolas" , 15))
        break

    elif player5.pos() >= (300 , -400):
        player5.penup()
        winannouncer.color("springgreen")
        winannouncer.write("Light green wins" , font=("consolas" , 15))
        break

    elif player6.pos() >= (300 , -400):
        player6.penup()
        winannouncer.color("cyan")
        winannouncer.write("Cyan wins" , font=("consolas" , 15))
        break

    else:
        player1.forward(dice1)
        player2.forward(dice2)
        player3.forward(dice3)
        player4.forward(dice4)
        player5.forward(dice5)
        player6.forward(dice6)

turtle.done()
