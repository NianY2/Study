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
        i = -1
        price = 0
        while i != len(cost)-1:
            if i == len(cost)-2 or cost[i+1] < cost[i+2]:
                print(1,cost[i+1])
                price += cost[i+1]
                i+=1
            else:
                print(2,cost[i+2])
                price += cost[i+2]
                i+=2

        return  price
if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10,15,20])) # 15
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) #6