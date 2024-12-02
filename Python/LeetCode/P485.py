"""
https://leetcode.cn/problems/max-consecutive-ones/description/
485. 最大连续 1 的个数
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        num = 0
        for i in nums:
            if i == 1:
                num += 1
            else:
                ans = max(ans,num)
                num = 0
        ans = max(ans, num)
        return  ans

if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3