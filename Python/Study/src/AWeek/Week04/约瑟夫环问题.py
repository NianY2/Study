'''
实例 6.6 约瑟夫环问题
有20个人围坐在一张圆桌周围，
从第1个人开始报数，数到3的那个人出列，
他的下一个人又从1开始报数，数到3的那个人又出列；
依此规律重复下去，直到圆桌周围的人数少于3时结束，
循环输出每次出列的人和剩下的人的序号。
'''
list1 = [i for i in range(1,21)]
num1 = 0
while len(list1) >= 3:
    num1 += 2
    num1 = num1 % len(list1)
    print(list1.pop(num1),end=" ")
