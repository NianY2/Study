"""
189. 轮转数组
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
https://leetcode.cn/problems/rotate-array/description/
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        n = len(nums)
        k = k % n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        return  nums


if __name__ == '__main__':
    print(Solution().rotate([1,2,3,4,5,6,7],3)) # [5,6,7,1,2,3,4]
    print(Solution().rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]
