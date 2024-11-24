"""
3232. 判断是否可以赢得数字游戏
https://leetcode.cn/problems/find-if-digit-game-can-be-won/description/
"""
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        n1,n2 = 0,0
        for i in nums:
            if i < 10:
                n1 += i
            else:
                n2 += i
        return  n1 != n2

if __name__ == '__main__':
    print(Solution().canAliceWin([1, 2, 3, 4, 10])) # Flase
    print(Solution().canAliceWin([1,2,3,4,5,14])) # True
    print(Solution().canAliceWin( [5,5,5,25])) # True
