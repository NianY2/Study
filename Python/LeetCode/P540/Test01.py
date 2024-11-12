"""
540. 有序数组中的单一元素
https://leetcode.cn/problems/single-element-in-a-sorted-array/description/?envType=daily-question&envId=2024-11-10
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (r+l) // 2
            print(mid)
            # mid ^ 1 偶数加1 奇数减1
            if nums[mid] == nums[mid^1]:
                l = mid + 1
            else:
                r = mid

        return  nums[l]



if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # 2
    print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))  # 10