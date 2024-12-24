"""
@Date: 2021/6/19 16:21:15
@Software: PyCharm
@Author: CY
"""

import time
import random
from turtle import *

# 绘制初始烟花线条的函数
def draw_firework(count, dis, ang):
    """
    count：线条数量
    dis：线条长度
    ang：线条之间的角度
    """
    for c in range(count):
        forward(dis)
        left(ang)

def draw_logo():
    # 加载图片到turtle
    screen.register_shape("./img/logo.gif")
    logo = Turtle(shape="./img/logo.gif")
    logo.penup()
    logo.goto(0, 150)  # 校徽居中显示
    logo.pendown()

def write_wishes():
    wishes = Turtle(visible=False)
    wishes.speed(0)
    wishes.penup()
    wishes.goto(-300, -250)  # 文本居中显示
    wishes.pendown()
    wishes.color("white")
    wishes.write("广州商学院25周年\n祝愿GCC：积历史之厚蕴，更展宏图！再谱华章！", font=("Arial", 16, "normal"))
    wishes.hideturtle()

def draw(lis):
    pensize(1)  # 设置画笔粗细为 1
    for t in range(repeat_num):  # 循环 repeat_num 次绘制烟花线条
        for li in lis:  # 遍历每个烟花参数列表
            x, y, col, dis, ang, add, count = li
            # 上一个烟花线条绘制完毕后移动画笔到下一个烟花绘制的开始位置，每次循环向左移动 add 的一半
            penup(), goto(x - t * add / 2, y), pendown()
            color('black', col)  # 设置画笔颜色为黑色，并设置填充颜色为传入的颜色
            begin_fill()  # 开始填充
            setheading(0)  # 设置方向为 0
            draw_firework(count, t * add + init_length, ang)  # 线条长度每轮循环增加 add，模拟烟花爆炸效果
            end_fill()  # 结束填充
        update()  # 全部烟花线条绘制完成后更新画面
        time.sleep(0.015)  # 暂停 0.015 秒
        clear()  # 清除画面

    pensize(2)  # 设置画笔粗细为 2
    for t in range(repeat_num):  # 再次进行 repeat_num 次循环绘制烟花爆炸后的点光影
        for li in lis:  # 遍历每个烟花参数列表
            x, y, col, dis, ang, add, count = li  # 获取参数
            pencolor(col)  # 设置画笔颜色
            count = int(count / 4)  # 计算爆炸点的数量，值越大点越密集
            radius = dis / 2 - 10 + t * 2  # 计算爆炸点圆的半径
            # 确定绘制圆的起始位置，爆炸线条中心点为(x+init_length/2，y)，以此点为圆心绘制半径为dis/2-10+t*2的圆，可得绘制的起始点坐标
            penup(), goto(x + init_length / 2 - radius, y), pendown()
            setheading(-90)  # 设置方向为-90
            for i in range(count):  # 循环绘制多个爆炸点
                penup()  # 抬笔
                circle(radius, 360 / count - 1)  # 绘制360 / count - 1度的圆弧，用于移动到下一个爆炸点位置
                pendown()  # 落笔
                circle(radius, 1)  # 落笔绘制1弧度的圆，作为爆炸点
        update()  # 更新画面
        time.sleep(0.03)  # 暂停 0.03 秒
        clear()  # 清除画面

def main(cols):
    while True:  # 无限循环
        fires = random.randint(10, 15)  # 生成随机的烟花数量
        need_list = []  # 创建存储烟花参数的列表
        for f in range(fires):  # 循环生成每个烟花的参数
            startx, starty = random.randint(-350, 350), random.randint(-100, 250)  # 随机起始位置
            ccol = random.choice(cols)  # 随机选择颜色
            dist = random.randint(init_length+20, init_length+50)  # 随机线条长度
            if dist <= 60:  # 根据长度设置角度
                angle = 171
            else:
                angle = random.choice([174, 175, 176])
            add = (dist - init_length) / repeat_num  # 计算每次循环增加的线条长度
            count = int(360 / (180 - angle))  # 计算线条数量
            need_list.append([startx, starty, ccol, dist, angle, add, count])  # 添加到列表
        draw(need_list)  # 绘制烟花
        clear()  # 清除画面

if __name__ == '__main__':
    try:
        init_length = 50  # 初始线条长度
        repeat_num = 10  # 循环次数
        setup(810, 605)  # 设置窗口大小
        screensize(800, 600, 'black')  # 设置画布大小及背景颜色
        hideturtle()  # 隐藏画笔
        colors = ['red', 'blue', 'yellow', 'white',
                  'green', 'orange', 'purple', 'seagreen',
                  'indigo', 'cornflowerblue']
        tracer(False)  # 不跟踪画笔移动轨迹
        screen = Screen()
        draw_logo()
        write_wishes()
        main(colors)
    except Exception as e:
        print(e)



