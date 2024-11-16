"""
62. 不同路径
https://leetcode.cn/problems/unique-paths/description/?envType=study-plan-v2&envId=dynamic-programming
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
排列组合

"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C(m+n-2,n-1) = A(m+n-2,n-1)/A(m+n-2,m+n-2)
        # return math.perm(m+n-2,n-1)//math.perm(m+n-2,m+n-2)

if __name__ == '__main__':
    print(Solution().uniquePaths(3,7)) # 28
    print(Solution().uniquePaths(3, 2))  # 3
    print(Solution().uniquePaths(7, 3))  # 28
    print(Solution().uniquePaths(3, 3))  # 6