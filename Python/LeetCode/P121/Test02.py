from typing import List

"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=dynamic-programming
优化2：记最小值，后续只需要减前面的最小值即可
则最大利润为(该天的股价-前面天数中最小的股价)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,cost = 0, float("+inf")
        for i in prices:
            cost = min(i,cost)
            profit = max(profit,i-cost)
        return  profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))