def menu():
    print('''\n欢迎使用PYTHON学生通讯录
        1：添加学生
        2：删除学生
        3：修改学生信息
        4：搜索学生
        5：显示全部学生信息
        6：退出并保存\n''')

dic = {'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}
print(dic)
menu()
while True:
    order = input()
    if order == "1":
        # 添加学生。如果该姓名已存在，则输出“该生信息已存在，无需添加！”；如果该姓名不存在
        name = input("姓名：")
        if name in dic:
            print("该生信息已存在，无需添加！")
        else:
            dic[name] = [input("电话："),input("学院：")]
        menu()
    elif order == "2":
        # 删除学生。如果该姓名已存在，则删除该生信息；如果该姓名不存在，直接输出“ERROR！”；
        try:
            del  dic[input("姓名：")]
        except KeyError:
            print("ERROR！")
        menu()
    elif order == "3":
        # 进行修改学生信息。输入姓名，如果该姓名已存在，则继续输入电话，学院信息，
        # 并输出“Success”的提示信息，如果不存在，给出“No Record”提示信息。
        name = input("姓名：")
        if name in  dic:
            dic[name] = [input("电话："),input("学院：")]
        else:
            print("No Record")
        menu()
    elif order == "4":
        # 搜索学生，如果该姓名已存在，则输出该生信息；若不存在，则输出“No Record”提示信息；
        try:
            print(dic[input("姓名：")])
        except KeyError:
            print("No Record")
        menu()
    elif order == "5":
        # 显示全部学生信息；
        print(dic)
        menu()
    elif order == "6":
        exit()

