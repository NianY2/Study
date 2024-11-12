"""
3258. 统计满足 K 约束的子字符串数量 I
https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/?envType=daily-question&envId=2024-11-12
10101 1

1 10 101 1010(x)
0 01 010 0101(x)
1 10 101
0 01
1
"""


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = [0] * 2  # count[i]表示窗口内字符i的个数, 初始化为0
        left = 0  # 滑动窗口左边界，初始为0
        res = 0  # 结果，初始为0
        for right, char in enumerate(s):  # 枚举窗口右边界，找到以右边界为结尾满足条件的最长子串[left, right]
            count[int(char)] += 1  # 更新right指向的字符的个数
            while count[0] > k and count[1] > k:  # 不断右移左边界直到满足条件
                count[int(s[left])] -= 1  # 更新left指向的字符的个数
                left += 1
            res += right - left + 1  # [left,right]以右边界为结尾满足条件的最长子串，其中的right-left+1个以右边界结尾的子串都满足条件
        return res



if __name__ == '__main__':

    print(Solution().countKConstraintSubstrings("10101",1)) # 12
    print(Solution().countKConstraintSubstrings("1010101", 2)) # 25
    print(Solution().countKConstraintSubstrings("11111", 1)) #15