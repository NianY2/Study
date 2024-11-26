"""
任务描述
输入一系列以逗号分隔的英文人名，其中包含重复的名字，
请将其中重复的名字去掉，输出包含不重复人名的列表，名字出现顺序与输入顺序相同。

输入格式
一系列以逗号分隔的英文人名

输出格式
包含不重复人名的列表，名字出现顺序与输入顺序相同

示例 1
输入：
Calvin,bob,ada,McCord,Smith,Babbs,Calvin,Smith
输出：
['Calvin', 'bob', 'ada', 'McCord', 'Smith', 'Babbs']
"""
list1 = input().split(",")
res = []
for i in list1:
    if i not  in res:
        res.append(i)
print(res)

