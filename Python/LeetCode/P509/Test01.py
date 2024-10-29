"""
斐波那契数
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
1 1
2 1
3 2
4 3
5 5
"""
class Solution:
    def fib(self, n: int) -> int:
        p = 0
        r = 0
        for i in range(1,n+1):
            q = p
            p = r
            r = q + p
            if i == 1:
                r = 1
        return  r

if __name__ == '__main__':
    print(Solution().fib(5))