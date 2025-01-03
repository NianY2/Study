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
        k = k % len(nums)

        for i in range(k):
            nums.insert(0,nums.pop())
        return nums


if __name__ == '__main__':
    print(Solution().rotate([1,2,3,4,5,6,7],3)) # [5,6,7,1,2,3,4]
    print(Solution().rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]
