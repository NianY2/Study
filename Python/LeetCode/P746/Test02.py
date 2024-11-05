"""
746. 使用最小花费爬楼梯
https://leetcode.cn/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=dynamic-programming

给你一个整数数组 cost ，
其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        print(dp)
        return dp[n]

if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([]))
    print(Solution().minCostClimbingStairs([10, 15]))  # 10
    print(Solution().minCostClimbingStairs([10,15,20])) # 15
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) #6