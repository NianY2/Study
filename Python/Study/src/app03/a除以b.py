# 输出实数a除以b的结果，计算结果四舍五入，保留2位小数。
# 当用户输入b为0时输出除零错误
# 其他情况下输出一个保留2位小数的实数


a = float(input())
b = float(input())
if b == 0:
    print("除零错误")
else:
    print(round(a/b,2))
