"""
661. 图片平滑器
https://leetcode.cn/problems/image-smoother/description/?envType=daily-question&envId=2024-11-18
"""
import copy
from typing import List


class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        n2 = len(img[0])
        # img2 = copy.deepcopy(img) # 深拷贝消耗性能
        # img2 = [[0]*n2]*n # 会创建一个所有行都引用同一个列表地址的二维列表，
        img2 = [[0] * n2 for _ in range(n)]
        for k,v in enumerate(img):
            for k2,v2 in enumerate(v):
                sum = 0
                num = 0
                if k - 1 >= 0:
                    sum+=img[k-1][k2]
                    num+=1
                    if k2 - 1 >= 0:
                        sum+=img[k-1][k2-1]
                        num+=1
                    if  k2+1 < n2:
                        sum+=img[k-1][k2+1]
                        num+=1
                if k+1 < n:
                    sum+=img[k+1][k2]
                    num+=1
                    if k2 - 1 >= 0:
                        sum+=img[k+1][k2-1]
                        num+=1
                    if  k2+1 < n2:
                        sum+=img[k+1][k2+1]
                        num+=1
                if k2 - 1 >= 0:
                    sum+=img[k][k2-1]
                    num+=1
                if  k2+1 < n2:
                    sum+=img[k][k2+1]
                    num+=1
                sum += v2
                num += 1
                img2[k][k2] = sum//num
        return  img2

if __name__ == '__main__':
    print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]])) # [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
    print(Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]])) # [[137,141,137],[141,138,141],[137,141,137]]

