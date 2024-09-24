# 119. 杨辉三角 II
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 使用滚动数组的思想优化空间复杂度。
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rpeList = []
        for i in range(0,rowIndex+1):
            curList = []
            for k in range(0,i+1):
                if k == 0 or k == i:
                    curList.append(1)
                else:
                    curList.append(rpeList[k-1]+rpeList[k])
            rpeList = curList
        return rpeList
if __name__ == '__main__':
    print(Solution().getRow(3))