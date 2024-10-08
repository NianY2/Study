from typing import List

"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=dynamic-programming
优化1：即第 1 天成本更低，那么我们一定不会选择在第 2 天买入。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,cost = 0, float("+inf")

        for i in range(len(prices)):
            if prices[i] > cost:
                continue
            for j in range(i+1,len(prices)):
                price = prices[j] - prices[i]
                profit = price if price > profit else profit
        return  profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))