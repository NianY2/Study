"""
任务描述
对一个有序的整数序列，现在要将一个整数插入进去，并保证该序列仍然有序。请输出这个数要插入的位置
第一行输入若干个整数，以空格间隔，本题保证用例中输入的数值顺序一定是从小到大，原始列表中无重复数据
第二行输入一个整数n
将整数序列放入列表ls
如果ls中已经存在n，则不插入该数，输出 Fail以及ls列表
若ls中可以插入n，输出插入位置（从0开始计数），以及插入后的ls列表
示例
输入：
1 2 3 5
4
输出：
3
[1, 2, 3, 4, 5]
"""
ls = input().split()
n = int(input())
ls = [int(i) for  i in  ls]

l = 0
r = len(ls) - 1
while l <= r:
    mid = (r+l) // 2
    if ls[mid] < n:
        l = mid + 1;
    else:
        r = mid - 1;
if l == len(ls):
    print(l)
    ls.insert(l, n)
elif ls[l] == n:
    print("Fail")
else:
    print(l)
    ls.insert(l, n)
print(ls)