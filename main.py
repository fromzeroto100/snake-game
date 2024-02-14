from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
turtle = Turtle()


all_turtles = []

for turtle_index in range(0,3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.position(x=0, y=20 + 20)

































screen.exitonclick()