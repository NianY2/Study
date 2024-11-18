"""
如果一个数 p 是个质数，同时又是整数 a 的约数，则 p 称为 a 的一个质因数。
请问 2024 有多少个质因数。
"""
def test(n):
    res = 0
    ans = []
    for i in range(2,n+1):
        if n % i != 0:
            continue
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False
        if flag:
            res += 1
            ans.append(i)
    print(ans)
    return res
if __name__ == '__main__':
    print(test(2024))