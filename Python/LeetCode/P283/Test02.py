"""
283. 移动零
https://leetcode.cn/problems/move-zeroes/description/
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
双指针
[0,1,0,3,12]
 l(r)
 l r
[1,0,0,3,12]
   l r
   l   r
[1,3,0,0,12]
     l    r
[1,3,12,0,0]
没有0 时l和r 会一起加
[1,1,0,3,12]
 l(r)
  l(r)
     l(r)
     l r
[1,1,3,0,12]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l=r=0
        while r < n:
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            r+=1
        return  nums

if __name__ == '__main__':
    print(Solution().moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]
    print(Solution().moveZeroes([0]))  # [0]
    print(Solution().moveZeroes([0,0,1]))  # [1,0,0]
