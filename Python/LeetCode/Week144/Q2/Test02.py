"""
Q2. 两个字符串的切换距离
https://leetcode.cn/contest/biweekly-contest-144/problems/shift-distance-between-two-strings/
"""                                           
from typing import List
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        ans = 0
        for k,v in enumerate(s):
            n1=n2=0
            ans+=min(n1,n2)
            vn = ord(v) - ord("a")
            tn = ord(t[k]) - ord("a")
            if vn < tn:
                n1 = sum(nextCost[vn:tn])
                n2 = sum(previousCost[tn+1:]+previousCost[0:vn+1])
            elif vn > tn:
                n2 = sum(previousCost[vn:tn:-1])
                n1 = sum(nextCost[vn:]+nextCost[:tn])
            ans+=min(n1,n2)
        return ans
if __name__ == '__main__':
    # print(Solution().shiftDistance(s="z", t="a",
    #                                nextCost=[100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #                                          0, 1],
    #                                previousCost=[1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #                                              0, 0, 0]))
    print(Solution().shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) #2
    print(Solution().shiftDistance(s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])) # 31
    # print(chr((ord('z')+ 1 - ord('a') )% 26 + ord('a')))
    # a < b
    # print(ord("b")-ord("a"))
    # print(26+(ord("a")-ord("b")))
    # v = "a"
    # k=0
    # t = ["b"]
    # n1 = sum(nextCost[ord(v) - ord("a"):ord(t[k]) - ord(v) - ord("a")])
    # n2 = sum(nextCost[26 + (ord(v) - ord(t[k])) - ord("a"):ord(v) - ord("a"):-1])
