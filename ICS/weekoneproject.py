from turtle import *
import random
bot = Turtle()
bot.speed(-1)
bot.color("red")
bot.fillcolor("blue")


def square(x, y):
    bot.penup()
    bot.setpos(x, y)
    bot.pendown()
    thing = random.randint(0, 100)
    bot.begin_fill()
    for element in range(4):
        bot.forward(thing)
        bot.right(90)
    bot.end_fill()


def main():
    square(random.randint(-300, 300), random.randint(-300, 300))


while True:
    main()
