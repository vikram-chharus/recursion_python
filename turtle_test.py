from random import randint
import turtle, randomcolor 
MAX_LENGTH = 250
INCREMENT = 10

def draw_spiral(a_turtle, line_length):
    if line_length> MAX_LENGTH:
        return 
    a_turtle.color(randomcolor.RandomColor().generate())
    a_turtle.forward(line_length)
    a_turtle.right(90)
    a_turtle.left(70)
    a_turtle.backward(line_length)
    draw_spiral(a_turtle, line_length+ INCREMENT)


charlie = turtle.Turtle(shape="turtle")
charlie.pensize(5)
charlie.color("red")
charlie.circle(20)
draw_spiral(charlie, 10)
turtle.done()