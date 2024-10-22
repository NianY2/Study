"""
  在军训过程中，学员训练队列表演，一切听从教官的口号。
  队列训练有出列、入列、最后一名学生报数，求队列长度，
  判断队伍是否为空等操作。请编写程序模拟队列操作。
# 1.集合（入列）
# 2.出列(从队尾出列)
# 3.最后一名学生报数\
# 4.队伍长度
# 5.退出
"""
list1=[]
while True:
    oder=int(input("教官发指令："))
    if oder ==1:
        list1.insert(0,input("学生姓名："))
    elif oder ==2:
        print(list1.pop()+"出列")
    elif oder==3:
        print(f"{list1[len(list1)-1]}报数{len(list1)}")
    elif oder==4:
        print(f"队伍长度{len(list1)}")
    elif oder == 5:
        print("退出")
        exit()