# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，用户输入一个月份数，
# 计算并在一行内输出该月的兔子总对数以及前一个月与本月兔子数量的比值（计算并观察一下这个比值的数值是多少），
# 比值结果保留小数点后3位，数字间用空格分隔。

month = int(input())
oldRabbit = 0
age1Rabbit = 1
age2Rabbit = 0
previousMonth = 0
nowMonth = 1
for i in range(2,month+1):
    previousMonth = nowMonth

    oldRabbit+=age2Rabbit
    age2Rabbit=age1Rabbit
    age1Rabbit=oldRabbit

    # print(oldRabbit+age2Rabbit+age1Rabbit)
    nowMonth = oldRabbit+age2Rabbit+age1Rabbit
print(nowMonth,f"{(previousMonth/nowMonth):.3f}")