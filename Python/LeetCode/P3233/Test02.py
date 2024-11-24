"""
3233. 统计不是特殊数字的数字数量
https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/description/?envType=daily-question&envId=2024-11-22
只有质数的平方 p**2才是特殊数字
预处理 31622 内的质数
"""



class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = 0
        if l == 1:
            ans+=1
            l = 2
        for i in range(l,r+1):
            g = i**0.5
            if g == int(g):
                for j in range(2,int(g)):
                    if  i%j==0:
                        ans+=1
                        break
                continue
            ans+=1
        return  ans

if __name__ == '__main__':
    print(Solution().nonSpecialCount(1, 2))  # 2
    print(Solution().nonSpecialCount(5,7)) #3
    print(Solution().nonSpecialCount(4,16))#11