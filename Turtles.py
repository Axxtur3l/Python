from turtle import Turtle, Screen
from random import randint, choice as randomizer

colors = ['red', 'pink', 'purple', 'green']
# while True:
#  forward(20)
#  penup()
#  forward(20)
#  pendown()

# input()
class MyTurtle(Turtle):
    def random_shape(self, x, y):
        self.color(randomizer(colors))

        self.penup()
        self.setposition(randint(-200, 200), randint(-200,200))
        self.pendown()
        self.circle(50, steps = randint(4,12))



    def __init__(self):
        super().__init__()
        self.random_shape(0, 0)
        self.onclick(self.random_shape)


x = MyTurtle()

x.forward(50)

y = MyTurtle()

y.backward(50)

screen = Screen()

screen.mainloop()