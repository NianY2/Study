"""
3216. 交换后字典序最小的字符串
https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/
给你一个仅由数字组成的字符串 s，在最多交换一次 相邻 且具有相同 奇偶性 的数字后，返回可以得到的
字典序最小的字符串
如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。
"""
class Solution:
    def getSmallestString(self, s: str) -> str:
        l1 = list(s)
        for i in range(1,len(l1)):
            num1 = int(l1[i])
            num2 = int(l1[i-1])
            # if ((num1 % 2 == 0) == (num2 % 2 == 0)) and (num1 < num2):
            # 相同奇偶性可以 (s[i] + s[i+1]) % 2 == 0
            if (num1+num2 % 2 == 0) and (num1 < num2):
                p = l1[i]
                l1[i] = l1[i-1]
                l1[i-1] = p
                break
        return  "".join(l1)

if __name__ == '__main__':
    print(Solution().getSmallestString("45320"))
    print(Solution().getSmallestString("001"))
    print(Solution().getSmallestString("0031"))