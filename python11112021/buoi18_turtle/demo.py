import turtle
import time


s = turtle.getscreen()

t = turtle.Turtle()

# t.penup()
t.speed("slow")  # Tốc độ
turtle.bgcolor("blue")

t.goto(100, 100)
t.right(90)
t.forward(100)
t.goto(-100, -100)
t.left(90)
t.backward(100)
time.sleep(5)
t.clear()


turtle.bgcolor("yellow")
t.pencolor("red")
# Vẽ hình bình hành
t.goto(0, 100)
t.goto(50, 100)
t.right(200)
t.goto(-50, -100)
t.left(200)
time.sleep(5)
t.clear()


turtle.bgcolor("white")
t.circle(15)

time.sleep(5)  # ngủ 5s
t.hideturtle()
