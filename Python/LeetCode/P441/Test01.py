"""
441. 排列硬币
https://leetcode.cn/problems/arranging-coins/description/?envType=problem-list-v2&envId=binary-search
暴力
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 0
        colNum = 1
        while n >= colNum:
            n -= colNum
            row+=1
            colNum+=1
        return row

if __name__ == '__main__':
    print(Solution().arrangeCoins(1))