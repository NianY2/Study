"""
62. 不同路径（排列组合）
https://leetcode.cn/problems/unique-paths/description/?envType=study-plan-v2&envId=dynamic-programming
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
因为机器到底右下角，向下几步，向右几步都是固定的，

从左上角到右下角的过程中，我们需要移动 m+n−2 次，其中有 m−1 次向下移动，n−1 次向右移动。
因此路径的总数，就等于从 m+n−2 次移动中选择 m−1 次向下移动的方案数，即组合数：
所以有 组合：C(m−1,m+n−2)
C(n,m) = A(n,m)/A(m,m) = n(n-1)。。。(n-m+1)/m(m-1)。。。1
"""
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 方法1
        return  math.comb(m+n-2,n-1)

        # 方法2
        # C(40,3) = A(40,3)/A(3,3) = 40*39*38
        # return math.perm(m + n - 2, n - 1) // math.perm(n-1,n-1)


        # 方法3
        # a1 = 1
        # a2 = 1
        # # for i in range(m + n - 2, m + n - 2 - n + 1+1-1, -1):
        # for i in range(m + n - 2,m - 1,-1):
        #     a1*=i
        # # for i in range(1,n-1+1):
        # for i in range(1, n):
        #     a2*=i
        # return  a1//a2


if __name__ == '__main__':
    print(Solution().uniquePaths(3,7)) # 28
    print(Solution().uniquePaths(3, 2))  # 3
    print(Solution().uniquePaths(7, 3))  # 28
    print(Solution().uniquePaths(3, 3))  # 6