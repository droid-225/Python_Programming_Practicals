import turtle


def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_smiley_face():
    turtle.speed(3)
    turtle.bgcolor("white")

    # Draw face
    draw_circle("yellow", 0, 0, 100)

    # Draw eyes
    draw_circle("black", -35, 40, 15)
    draw_circle("black", 35, 40, 15)

    # Draw mouth
    turtle.penup()
    turtle.goto(-40, -20)
    turtle.pendown()
    turtle.pensize(5)
    turtle.setheading(-60)
    turtle.circle(40, 90)

    turtle.hideturtle()
    turtle.done()


# Draw the smiley face
draw_smiley_face()
