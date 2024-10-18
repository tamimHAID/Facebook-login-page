import math
import turtle

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(4 * k)

turtle.speed(0)
turtle.bgcolor("black")

for i in range(6000):
    turtle.goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        turtle.color("red")
    turtle.goto(0, 0)

turtle.done()
