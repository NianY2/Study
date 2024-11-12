"""
面试题 17.14. 最小K个数
https://leetcode.cn/problems/smallest-k-lcci/
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
"""
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return  arr[0:k]

if __name__ == '__main__':
    print(Solution().smallestK([1,3,5,7,2,4,6,8],4))