ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
s = input()        # 输入一个字符
# 当输入为"1"时，输出元素为0-9的3次方的列表 [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
if s == '1':
    print([i**3 for i in  range(10)])
# 当输入为"2"时，输出元素为0-9中偶数的3次方的列表 [0, 8, 64, 216, 512]
elif s == '2':
    print([i**3 for i in  range(0,10,2)])
 # 当输入为"3"时，输出元素为元组的列表，元组中元素依次是0-9中的奇数和该数的3次方[(1, 1), (3, 27), (5, 125), (7, 343), (9, 729)]
elif s == '3':
    print([(i,i**3) for i in range(1,10,2)])
    pass
# 当输入为"4"时，将ls中每个元素单词首字母大写输出['The lord of the rings', 'Anaconda', 'Legally blonde', 'Gone with the wind']
elif s == '4':
    print([i.capitalize() for i in  ls])
    pass
# 当输入为其他字符时，执行以下语句
# 输入其他字符，输出“结束程序”
else:
    print("结束程序")