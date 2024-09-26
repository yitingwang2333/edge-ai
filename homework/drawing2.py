import turtle  
  
# 设置画布和画笔  
screen = turtle.Screen()  
screen.title("花朵绘制")  
screen.bgcolor("white")  
  
flower = turtle.Turtle()  
flower.speed(0)  # 设置画笔速度  
  
# 定义一个绘制花瓣的函数（这里用扇形代替）  
def draw_petal(color, radius, start_angle, end_angle):  
    flower.color(color)  
    flower.begin_fill()  
    flower.left(start_angle)  
    flower.circle(radius, end_angle - start_angle)  
    flower.left(180 + start_angle)  
    flower.end_fill()  
  
# 绘制一朵花  
def draw_flower(center_x, center_y, size):  
    flower.penup()  
    flower.goto(center_x, center_y)  
    flower.pendown()  
      
    # 绘制花瓣，这里用简单的扇形来模拟  
    # 你可以根据需要调整花瓣的数量、大小、起始和结束角度  
    draw_petal("red", size, 0, 60)  
    draw_petal("pink", size, 60, 120)  
    draw_petal("yellow", size, 120, 180)  
    draw_petal("red", size, 180, 240)  
    draw_petal("pink", size, 240, 300)  
    draw_petal("yellow", size, 300, 360)  
  
# 绘制几朵不同的花  
draw_flower(-100, 0, 50)  
flower.penup()  
flower.goto(-50, -50)  # 移动画笔到新位置以避免重叠  
flower.pendown()  
draw_flower(0, 0, 60)  
flower.penup()  
flower.goto(50, 50)  # 再次移动画笔到新位置  
flower.pendown()  
draw_flower(100, 0, 70)  
  
# 结束绘图  
flower.hideturtle()  
turtle.done()
