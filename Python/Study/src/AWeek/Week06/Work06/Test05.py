"""
请设计篮球比赛赛程安排，小组赛有四支队伍，分主客场，求要比赛多少场，对战情况如何？
"""
num = 0
for i in range(4):
    num += i
print(num*2)