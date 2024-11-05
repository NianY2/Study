"""
P198
打家劫舍
https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=dynamic-programming
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        # for i in range(s):
        #     dp[i+1] = max(dp[i-2]+nums[i],dp[i-3]+nums[i-1])
        print(dp)
        return  dp[size-1]
if __name__ == '__main__':
    print(Solution().rob([]))
    print(Solution().rob([1]))
    print(Solution().rob([1, 2]))
    print(Solution().rob([1,2,3,1]))  # 4
    print(Solution().rob([2,7,9,3,1])) #  12