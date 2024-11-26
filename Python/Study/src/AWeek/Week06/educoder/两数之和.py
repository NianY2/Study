"""
任务描述
给定一个整数列表 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的列表索引。
每种输入只需要对应一个答案。但是，你不能重复使用这个数组中同样位置的元素。
如果无解，输出Fail
输入格式
两行输入
第一行输入一组整数，以若干空格间隔，数据全部为int型。
第二行输入一个整数
输出格式
如果有解，输出第一组解（元素索引最小优先）。
如果无解，输出Fail

示例
输入：
3 4 5 6
9
输出：
0 3
"""
list1 = input().split()
target = int(input())
hashtable = dict()
res = "Fail"
res_index = len(list1)

for i,num in enumerate(list1):
    i = int(i)
    num = int(num)
    if target - num in hashtable:
        if res_index > min(hashtable[target - num],i):
            res_index = min(hashtable[target - num],i)
            res  = f"{min(hashtable[target - num],i)} {max(hashtable[target - num],i)}"
    hashtable[num] = i
print(res)