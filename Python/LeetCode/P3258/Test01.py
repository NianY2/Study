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
        n = len(s)
        res = 0
        for i in range(n):
            count = [0,0]
            for j in range(i,n):
                count[int(s[j])] += 1
                if count[0] > k and count[1] > k:
                    break
                res+=1
        return  res


if __name__ == '__main__':
    print(Solution().countKConstraintSubstrings("10101",1)) # 12
    print(Solution().countKConstraintSubstrings("1010101", 2)) # 25
    print(Solution().countKConstraintSubstrings("11111", 1)) #15