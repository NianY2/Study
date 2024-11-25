"""
665. 非递减数列
https://leetcode.cn/problems/non-decreasing-array/description/
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            x = nums[i]
            y = nums[i+1]
            if x > y:
                nums[i] = y
                if self.isSorted(nums):
                    return  True
                nums[i] = x
                nums[i+1] =x
                return self.isSorted(nums)
        return  True

    def isSorted(self,nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return  True

if __name__ == '__main__':
    print(Solution().checkPossibility([4,2,3])) # True
    print(Solution().checkPossibility([4,2,1])) # False
    print(Solution().checkPossibility([3,4,2,3]))  # False
