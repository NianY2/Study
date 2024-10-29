"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
1 1                     - 1
2 11 2                  - 2
3 111 12 21             - 3
4 1111 22 121 211 112   - 5
f(x) = f(x-1) + f(x-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        q = 0
        r = 1
        for i in range(1,n+1):
            p = q
            q = r
            r = p + q
        return  r
if __name__ == '__main__':
    # 1 <= n <= 45
    print(Solution().climbStairs(4))