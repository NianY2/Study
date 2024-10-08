"""
https://leetcode.cn/problems/counting-bits/?envType=problem-list-v2&envId=dynamic-programming
比特位计数
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = 0
        for i in str(bin(n)):
            if i == 1:
               cnt += 1
        print(cnt)

if __name__ == '__main__':
    Solution().countBits(3)
