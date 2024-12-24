from typing import List
"""
https://leetcode.cn/problems/find-indices-of-stable-mountains/
简单
"""

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(0,len(height)-1):
            if height[i] > threshold:
                ans.append(i+1)
        return  ans

if __name__ == '__main__':
    print(Solution().stableMountains([1,2,3,4,5],2)) # [3,4]