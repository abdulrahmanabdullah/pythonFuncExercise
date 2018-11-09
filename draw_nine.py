import turtle
import time
import random

list_color = ['red','green','blue']
def get_color(r):
    return r.color(random.choice(list_color))


# TODO: create window , make bgcolor randomly .
def set_color(t, colors):
    t.color(colors)

def create_window():
    t = turtle.Turtle()
    t.color("white")
    window = turtle.Screen()
    window.bgcolor('black')
    round_five_with_if(t)
    window.exitonclick()

# round five :
def round_five_without_if():
    r = turtle.Turtle()
    list = [4,4,4,2,2]
    for item in list :
        for x in range(item):
            move_forward(r,1)
        turn_left(r)
def move_forward(r,step):
    r.speed(1)
    r.width(4)
    for item in range(step):
        time.sleep(0.5)
        r.fd(30)


def round_five_with_if(r):
    is_done = True
    counter = 0
    track = 0
    while is_done :
        counter += 1
        move_forward(r, 1)
        r.color("black")
        if counter % 3 == 0 : # this take yellow color
            set_color(r,'yellow')
            track += 1 # first line track = 1 and second = 2 and the last line it's = 3
            turn_left(r)
            counter = 0
        elif track == 3 : # this take darkyellow
            set_color(r, 'darkblue')
            turn_left(r)
            move_forward(r, 2)
            r.left(360)
            is_done = False
        else: # this take red color .
            set_color(r, 'red')


def turn_left(r):
    r.lt(90)

# round_five_with_if()

create_window()
