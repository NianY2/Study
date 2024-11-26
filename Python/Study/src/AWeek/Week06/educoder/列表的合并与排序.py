"""
任务描述
读入两行，两行的格式一样，都是用空格分隔的若干个整数，将这些数合并到一个列表中，降序排列后输出整个列表。

提示：
list1 = list(map(int,input().split()))
#读入一行由空格分隔的整数，将其存入list1列表中

输入格式
输入为两行，两行格式一样，都是用空格分隔的若干个整数（整数个数可能为0个）。

输出格式
输出为一行，是元素按数值降序排列后的整数列表。
"""
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = [*list1,*list2]
list3.sort(reverse=True)
print(list3)