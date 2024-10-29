"""
第 N 个泰波那契数
泰波那契序列 Tn 定义如下：
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        ls1 = [0]
        for i in range(1,n+1):
            if i == 1 or i == 2:
                ls1.append(1)
                continue
            ls1.append(ls1[i-1]+ls1[i-2]+ls1[i-3])
        return ls1.pop()
if __name__ == '__main__':
    print(Solution().tribonacci(0))