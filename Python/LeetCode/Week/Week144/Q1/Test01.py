"""
Q1. 移除石头游戏
https://leetcode.cn/contest/biweekly-contest-144/problems/stone-removal-game/description/
"""


class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        num = 10
        while True:
            n -= num
            if n >= 0:
                num-=1
                ans = not ans
            else:
                break
        return  ans
if __name__ == '__main__':
    print(Solution().canAliceWin(1))