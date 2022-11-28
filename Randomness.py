from turtle import *

from random import randint, choice as randomizer

speed(0)

colors = ['red', 'pink', 'purple', 'green']

for i in range(100):
    penup()
    setposition(randint(-200,200), randint(-200,200))
    pendown()

    # color(randomizer(colors))
    pencolor(randomizer(colors))
    fillcolor(randomizer(colors))
    pensize(3)

    begin_fill()
    circle(randint(10,50), steps = randint(4,10))
    end_fill()

done()