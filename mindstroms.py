import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    x = turtle.Turtle()
    x.shape("turtle")
    x.color("yellow")
    x.speed(2)
    for i in range(1,37):
        draw_square(x)
        x.right(10)

    #y = turtle.Turtle()
    #y.shape("arrow")
    #y.color("blue")
    #y.circle(100)

    window.exitonclick()

draw_art()    
