# 119. 杨辉三角 II
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        resList = []
        for i in range(0,rowIndex+1):
            row = []
            for k in range(0,i+1):
                if k == 0 or k == i:
                    row.append(1)
                else:
                    row.append(resList[i-1][k-1]+resList[i-1][k])
            resList.append(row)
        return resList[rowIndex]
if __name__ == '__main__':
    print(Solution().getRow(3))