# 编写一个学生成绩转换程序，用户输入百分制的学生成绩，
# 成绩大于等于90且小于等于100的输出为A，
# 成绩大于或等于80且小于90的输出为B，
# 成绩大于或等于70且小于80的输出为C，
# 成绩大于或等于60且小于70的输出为D，
# 成绩小于60且大于等于0的输出为E，
# 如果输出的成绩大于100或小于0，输出data error!。
num = float(input())
if 90 <= num <= 100:
    print("A")
elif 80 <= num < 90:
    print("B")
elif 70 <= num < 80:
    print("C")
elif 60 <= num < 70:
    print("D")
elif 0 <= num <60:
    print("E")
else:
    print("data error!")