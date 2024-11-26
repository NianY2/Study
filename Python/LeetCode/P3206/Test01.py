from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        for i in range(len(colors)):
            if colors[i - 1] != colors[i] and colors[i] != colors[(i + 1) % len(colors)]:
                ans += 1
        return ans
if __name__ == '__main__':
    print(Solution().numberOfAlternatingGroups([1,1,1])) #0
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1]))  # 3
