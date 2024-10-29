"""
441. 排列硬币
https://leetcode.cn/problems/arranging-coins/description/?envType=problem-list-v2&envId=binary-search
数学
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        x**2 + x - 2n = 0
        b**2 - 4ac = 8n + 1 > 0
        x = (pow((8*n+1),0.5)- 1) // 2
        向下取整
        """
        return  int((pow((8*n+1),0.5)- 1) // 2)
if __name__ == '__main__':
    print(Solution().arrangeCoins(8))