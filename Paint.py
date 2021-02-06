import turtle

# setting players and screen
screen = turtle.Screen()
player = turtle.Turtle()
redp = turtle.Turtle()
greenp = turtle.Turtle()
yellowp = turtle.Turtle()
bluep = turtle.Turtle()

psize2 = turtle.Turtle()
psize5 = turtle.Turtle()
psize10 = turtle.Turtle()


# setting shape for color buttons
redp.shape("square")
yellowp.shape("square")
bluep.shape("square")
greenp.shape("square")
psize2.shape("square")
psize5.shape("square")
psize10.shape("square")
player.shape("circle")
player.shapesize(1)

# setting pen up for buttons
redp.penup()
yellowp.penup()
bluep.penup()
greenp.penup()
psize2.penup()
psize5.penup()
psize10.penup()


# setting colors
redp.color("red")
greenp.color("green")
bluep.color("blue")
yellowp.color("yellow")


# methods for color buttons
def red(x, y):
    player.color("red")


def green(x, y):
    player.color("green")


def yellow(x, y):
    player.color("yellow")


def blue(x, y):
    player.color("blue")

def goto(x, y):
    player.ondrag(None)
    player.goto(x, y)
    player.ondrag(goto)
def pensize2(x,y):
    player.pensize(2)
def pensize5(x,y):
    player.pensize(5)
def pensize10(x,y):
    player.pensize(10)
def teleportto(x,y):
    player.penup()
    player.goto(x,y)
    player.pendown()
def painter():
    # buttons location
    bluep.goto(75, -300)
    yellowp.goto((25, -300))
    greenp.goto(-25, -300)
    redp.goto(-75, -300)
    psize2.goto(-200, -300)
    psize5.goto(-250, -300)
    psize10.goto(-300, -300)

    # basic UI setup
    psize2.write("2" , align='center', move=True)
    psize5.write("5" , align='center', move=True)
    psize10.write("10" , align='center', move=True)

    # going a bit below the text so the text can be shown
    psize2.goto(-200, -315)
    psize5.goto(-250, -315)
    psize10.goto(-300, -315)


    # on click methods
    redp.onclick(red, btn=3)
    greenp.onclick(green, btn=3)
    yellowp.onclick(yellow, btn=3)
    bluep.onclick(blue, btn=3)
    psize2.onclick(pensize2, btn=3)
    psize5.onclick(pensize5, btn=3)
    psize10.onclick(pensize10, btn=3)
    screen.onclick(teleportto)
    player.ondrag(goto)


painter()

turtle.mainloop()
