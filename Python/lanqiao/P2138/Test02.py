"""
最优清零方案
https://www.lanqiao.cn/problems/2138/learning/
Dynamic Programming(dp)
"""
# s = input().split()
# ls =  input().split()
s = "4 2".split()
ls = "1 2 3 4".split()
N,K = int(s[0]),int(s[1])
data = list(map(int,ls))
ans = 0
i = 0
while i < N:
    if i + K -1 < N:
        minn = min(data[i:i+K])
        if minn > 0:
            for j in range(i,i+K):
                data[j] -= minn
                if data[j] == 0:
                    i = j
        ans += minn
    else:
        ans += sum(data)
        break
    i += 1
print(ans)