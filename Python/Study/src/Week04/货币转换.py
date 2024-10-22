"""
编写一个美元与人民币转换的程序，
用户输入金额和汇率（合理的汇率是正数），
输出转换为另一种货币表示的金额。
美元:'$'
人民币:'¥'
输入符合要求时输出一个带货币符号的数值（保留2位小数）
输入不符合要求时输出“Data error!”
第一行输入一个以货币符号结尾的正数，数值作为金额，货币符号表明货币种类
第二行输入一个浮点数作为汇率
输入：
58$
6.75
输出：
391.50¥
"""
money = input()
exchange_rate = float(input())
if exchange_rate < 0:
    print("Data error!")
    exit()
if money[-1] == "$":
    money =  float(money[:len(money) - 1]) * exchange_rate
    print(f"{money:.2f}¥")
elif money[-1] == "¥":
    money = float(money[:len(money) - 1]) / exchange_rate
    print(f"{money:.2f}$")
else:
    print("Data error!")



