"""
3243. 新增道路查询后的最短距离 I
https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/description/
"""
from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        neighbors = [[i+1] for  i in range(n)]
        neighbors[-1] = []
        res = []
        for (u,v) in queries:
            neighbors[u].append(v)
            res.append(self.bfs(n,neighbors))
        return  res

    def bfs(self,n:int,numerator:List[List[int]])->int:
        dist = [-1]*n
        dist[0] = 0

        # q = [0] # 队列
        while len(q) > 0:
            # x = q.pop(0)
            for y in numerator[x]:
                if dist[y] >= 0:
                    continue
                q.append(y)
                dist[y] = dist[x] + 1
        return dist[n-1]

if __name__ == '__main__':
    print(Solution().shortestDistanceAfterQueries(5,[[2, 4], [0, 2], [0, 4]]))  # [3, 2, 1]
    print(Solution().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))  # [3, 2, 1]
    print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]]))  # [1, 1]
    print(Solution().shortestDistanceAfterQueries(8, [[5,7],[0,6]]))  # [6, 2]
