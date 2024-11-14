money=5000000
name=input("请输入姓名：")


def cxye():
    global money
    print(f"余额：{money}￥")
    show()
def ck():
    global money
    money += int(input("变化金额（￥）："))
    print(f"存款成功-余额：{money}￥")
    show()
def qk():
    global money
    money -= int(input("变化金额（￥）："))
    print(f"取款成功-余额：{money}￥")
    show()

def tc():
    exit()

def show():
    global money
    print("{:-^40}".format("主菜单"))
    print(f'{name},您好，欢迎来到广商银行ATM')
    print("查询余额\t[输入1]")
    print("存款\t    [输入2]")
    print("取款\t    [输入3]")
    print("退出\t    [输入4]")
    print("请输入您的选择：")
    a=input()
    dict =  {
        "1":cxye,
        "2": ck,
        "3": qk,
        "4": tc,
    }
    dict[a]()
show()