"""
3232. 判断是否可以赢得数字游戏
https://leetcode.cn/problems/find-if-digit-game-can-be-won/description/
单数正加，双数反减，
胜在不等，零则必输！
"""
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return  sum(i  if i < 10 else -i for i in nums) != 0

if __name__ == '__main__':
    print(Solution().canAliceWin([1, 2, 3, 4, 10])) # Flase
    print(Solution().canAliceWin([1,2,3,4,5,14])) # True
    print(Solution().canAliceWin( [5,5,5,25])) # True
