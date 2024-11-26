"""
输入一个正整数 n，
先根据用户输入的用空格分隔的一系列地名创建一个集合my_set，
然后你将被要求读入 n 个输入（输入形式如下所示），
每得到一个输入后，根据输入进行操作。

add name:             # 在集合中加入元素name
print:                # 将集合转为列表，按元素升序排序后输出列表
del name:             # 删除集合中的元素name，当name不存在时，不能引发错误
update name:          # name为空格逗号分隔的字符串，将其转为集合，并用name中的元素修改集合MySet
clear:                # 清空集合
输入格式
第一行输入一个正整数 n

输出格式
每遇到“print”时，将集合转为列表，按元素升序排序后输出列表

示例
输入：
8
湖北 湖南 吉林
print
del 湖北
print
clear
add 江西
add 河北
update 北京 上海 天津 重庆
print

输出：
['吉林', '湖北', '湖南']
['吉林', '湖南']
['上海', '北京', '天津', '江西', '河北', '重庆']
"""
n = int(input())
my_set = set(input().split())
for i in range(n):
    strList = input().split()
    if strList[0] == "add":
        my_set.add(strList[1])
    elif strList[0] == "print":
        print(sorted(list(my_set)))
    elif strList[0] == "del":
        if strList[1] in my_set:
            my_set.remove(strList[1])
    elif strList[0] == "update":
        names = set(strList[1:])
        for i in names:
            my_set.add(i)
    elif strList[0] == "clear":
        my_set = set()
    # add name:  # 在集合中加入元素name
    # print:  # 将集合转为列表，按元素升序排序后输出列表
    # del name:  # 删除集合中的元素name，当name不存在时，不能引发错误
    # update name:  # name为空格逗号分隔的字符串，将其转为集合，并用name中的元素修改集合MySet
    # clear:  # 清空集合
