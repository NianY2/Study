"""
Q1. 最小正和子数组
https://leetcode.cn/contest/weekly-contest-425/problems/minimum-positive-sum-subarray/description/
"""
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mins = -1
        for n in range(l,r+1):
            for i in range(0,len(nums),n):
                if i+n > len(nums):

                    s = sum(nums[-n:])
                else:
                    s = sum(nums[i:i+n])
                if s > 0:
                    if mins == -1:
                        mins = s
                        continue
                    mins = min(mins,s)
        return  mins


if __name__ == '__main__':
    print(Solution().minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3)) # 1
    print(Solution().minimumSumSubarray(nums = [1, 2, 3, 4], l = 2, r = 4))  # 3
    print(Solution().minimumSumSubarray(nums=[-2], l=2, r=3))  # -1
    print(Solution().minimumSumSubarray(nums=[-2,2,-3,1], l=2, r=3))  # -1
    print(Solution().minimumSumSubarray(nums=[-13,-21,24,-3], l=1, r=4))  # 3