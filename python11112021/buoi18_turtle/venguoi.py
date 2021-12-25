import turtle as t
import time as ti


def rectangle(hor, ver, color):
    t.pendown()  # tạo con trỏ
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()


t.penup()
t.speed('slow')
t.bgcolor('cyan')

# Vẽ 2 bàn chân
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# 2 cẳng chân
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

# Vẽ bụng
t.goto(-90, 100)
rectangle(100, 150, 'red')

# Vẽ 2 cánh tay
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')


# Vẽ bàn tay
t.goto(-50, 120)
rectangle(15, 20, 'grey')
t.goto(-85, 170)
rectangle(80, 50, 'red')
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-60, 160)
rectangle(5, 5, 'black')
t.goto(-45, 155)
rectangle(5, 5, 'black')
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'black')
t.goto(-155, 130)
rectangle(25, 25, 'green')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'green')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())

ti.sleep(10)
t.hideturtle()
