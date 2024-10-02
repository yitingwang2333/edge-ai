import turtle
import random

# 设置颜色列表
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'lime', 'magenta']

# 画一个花瓣
def draw_petal(t, radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(60)

# 画一朵花
def draw_flower(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(6):
        t.color(random.choice(colors))  
        draw_petal(t, radius)

# 设置画布和turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(10)

# 画三朵花
draw_flower(t, -150, 0, 60)
draw_flower(t, 0, 0, 60)
draw_flower(t, 150, 0, 60)

# 完成
turtle.done()
