"""
最优清零方案
https://www.lanqiao.cn/problems/2138/learning/
80%
"""
# s = input().split()
# ls =  input().split()
s = "4 2".split()
ls = "1 2 3 4".split()


n,k = int(s[0]),int(s[1])
ls = list(map(int,ls))
res = 0
for i in range(len(ls)):
    if ls[i] == 0:
        continue

    mid = []
    mins = 1000000
    for j in range(k):
        if j+i >= n or ls[j+i] == 0 :
                break
        mins = min(mins,ls[j+i])
        mid.append(ls[j+i])

    if len(mid) == k:
        res += mins
        for j in range(k):
            ls[i+j] -= mins

    if ls[i] != 0:
        res += ls[i]
        ls[i] = 0

print(res)
