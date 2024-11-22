"""
山
https://www.lanqiao.cn/problems/2141/learning/
"""
import math

res = 0
for i in range(2022,2022222023):
    i = list(str(i))
    n = len(i)
    flag = True
    for k,v in enumerate(i[0:n//2+1]):
        if v != i[math.ceil(n//2)+k]:
            flag = False
            break
    if flag:
        res+=1

print(res)