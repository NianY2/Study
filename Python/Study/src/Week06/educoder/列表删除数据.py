"""
任务描述
从输入的列表ls中，删除指定的数据n，并保持其他数据顺序不变。

第一行输入一行以空格间隔的整数，并放入列表ls

第二行输入一个整数n

删除整数列表中的所有的n值，并输出删除后的列表

如果原输入列表中没有n，则输出NOT FOUND

示例 1
输入：
1 1 2 2 4 6 1
2

输出：
[1, 1, 4, 6, 1]

示例 2
输入：
18 9 0 7 6
-1

输出：
NOT FOUND
"""
ls = input().split()
ls = [int(i) for  i in ls]
n =  int(input())
if n not  in ls:
    print("NOT FOUND")
    exit()
while n in ls:
    ls.remove(n)
print(ls)
