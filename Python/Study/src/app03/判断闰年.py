# 写一个程序用于判断用户输入的年份是不是闰年，
# 如果是输出True，如果不是输出False。
# 1、若一个年份能被4整除，并且不能被100整除，根据闰年的规定，该年份是普通闰年。
year = int(input())
if year % 400 == 0:
    print(True)
elif year % 4 == 0 and year % 100 != 0:
    print(True)
else:
    print(False)