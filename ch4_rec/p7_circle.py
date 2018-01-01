import turtle
import math


def circle(alpha, radius, t):
    number_it = 360 // alpha
    len_ = radius * math.sqrt(2 * (1 - math.cos(alpha)))
    for _ in range(number_it):
        t.forward(len_)
        t.right(alpha)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    circle(5, 10, t)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
