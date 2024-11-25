"""
453. 最小操作次数使数组元素相等
https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/description/
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

使 n−1 个元素增加 1，也可以理解使 1 个元素减少 1
我们只需要计算将数组中所有元素都减少到数组中元素最小值所需的操作数
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        ans = 0
        for i in nums:
            ans += i - min_num
        return  ans


if __name__ == '__main__':
    print(Solution().minMoves([1,2,3])) # 3
    print(Solution().minMoves([1,1,1])) # 0
