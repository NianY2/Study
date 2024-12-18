"""
https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel =0
        for i,v in enumerate(s):
            if v in "aeiou":
                vowel += 1
            if i < k -1: # i 从0 开始
                continue
            ans = max(ans,vowel)
            # 滑出
            if s[i-k+1] in "aeiou":
                vowel -= 1
        return  ans
if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef",3)) # 3
    print(Solution().maxVowels("aeiou", 2))  # 2
    print(Solution().maxVowels("leetcode", 3))  # 2
    print(Solution().maxVowels("rhythms", 4))  # 0
    print(Solution().maxVowels("tryhard", 4))  # 1