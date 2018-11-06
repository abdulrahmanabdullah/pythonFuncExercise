import turtle
import time
import random

list_of_colors = ['red','green','blue']
def get_color(shape):
    return shape.color(random.choice(list_of_colors))

# interval waiting
def wait_before_go():
    time.sleep(0.3)


# turn left
def turn_left(turte_):
    turte_.left(90)


# stage One .
def round_one():
    r1 = turtle.Turtle()
    move_forward(r1, 4)
    r1.left(360)

def move_forward(move, times):
    move.speed(1)
    move.width(2)
    for i in range(times):
        move.fd(30)


# round two
def round_two():
    r1 = turtle.Turtle()
    move_forward(r1, 1)
    wait_before_go()
    r1.left(90)
    wait_before_go()
    move_forward(r1, 1)
    r1.right(90)
    wait_before_go()
    move_forward(r1, 1)
    r1.left(360)

def round_three():
    r = turtle.Turtle()
    # for i in range(3):
    #     move_forward(r , i)
    is_done = True
    counter = 0
    while is_done :
        counter += 1
        move_forward(r, 1)
        wait_before_go()
        if counter >= 3 :
            r.left(360)
            is_done = False


# round four :
def round_four():
    r = turtle.Turtle()
    # for i in range(5):
    #     move_forward(r, 1)
    #     wait_before_go()
    #     turn_left(r)
    #     move_forward(r, 1)
    #     wait_before_go()
    #     r.right(90)
    not_done = True
    counter = 0
    while not_done :
        counter += 1
        move_forward(r, 1)
        turn_left(r)
        wait_before_go()
        move_forward(r, 1)
        wait_before_go()
        r.rt(90)
        if counter >= 5 :
            not_done = False
    r.rt(360)



# round five :
def round_five_without_if():
    r = turtle.Turtle()
    list = [4,4,4,2,2]
    for item in list :
        for x in range(item):
            move_forward(r,1)
        turn_left(r)

def round_five_with_if():
    r = turtle.Turtle()
    is_done = True
    counter = 0
    track = 0
    while is_done :
        counter += 1
        move_forward(r, 1)
        r.color("black")
        if counter % 3 == 0 :
            track += 1 # first line track = 1 and second = 2 and the last line it's = 3
            turn_left(r)
            counter = 0
        elif track == 3 :
            turn_left(r)
            move_forward(r, 2)
            r.left(360)
            is_done = False
        else:
            get_color(r)


if __name__ == "__main__":
    round_one()
    round_two()
    round_three()
    round_four()
    round_five_with_if()
    round_five_without_if()
    time.sleep(5)
