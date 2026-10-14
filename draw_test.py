import turtle
import random
 
# 初始化画布和画笔
screen = turtle.Screen()
screen.bgcolor("black")  # 背景设为黑色
pen = turtle.Turtle()
pen.speed(0)  # 画笔速度最快（0为最快）
pen.pensize(2)
 
# 定义颜色列表（可自定义）
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
 
# 绘制螺旋
for i in range(360):
    pen.color(colors[i % len(colors)])  # 按索引循环取颜色
    pen.forward(i)                      # 前进距离随循环递增
    pen.right(61)                       # 右转角度（61度可形成紧密螺旋）
 
# 隐藏画笔并保持窗口
pen.hideturtle()
turtle.done()