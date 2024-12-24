"""
396. 旋转函数
https://leetcode.cn/problems/rotate-function/description/
给定一个长度为 n 的整数数组 nums 。
假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
返回 F(0), F(1), ..., F(n-1)中的最大值 。
生成的测试用例让答案符合 32 位 整数。
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        max_f = -999999999999999999999999
        def f():
            ans = 0
            for k,v in enumerate(nums):
                ans += k*v
            return ans


        for i in range(len(nums)):
            nums.insert(0,nums.pop())
            max_f = max(max_f,f())
        return  max_f

if __name__ == '__main__':
    print(Solution().maxRotateFunction([4,3,2,6])) # 26
    print(Solution().maxRotateFunction([100]))  # 0
