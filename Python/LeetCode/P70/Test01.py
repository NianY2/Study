"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
1 1                     - 1
2 11 2                  - 2
3 111 12 21             - 3
4 1111 22 121 211 112   - 5
f(x) = f(x-1) + f(x-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        ls1 = []
        for i in range(n):
            if i == 0:
                ls1.append(1)
                continue
            if i == 1:
                ls1.append(2)
                continue
            ls1.append(ls1[i-1]+ls1[i-2])
        return  ls1.pop()

if __name__ == '__main__':
    # 1 <= n <= 45
    print(Solution().climbStairs(4))