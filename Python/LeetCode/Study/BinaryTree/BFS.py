"""
广度优先搜索（BFS） Breath First Search
"""
from typing import List
from typing_extensions import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root:Optional[TreeNode]) -> List:
    res = []
    q = [root] # 先把根节点放进队列中
    while q:  # 当队列不为空时进入循环体
        current_node = q.pop(0)  # 取出队列的第一个节点
        res.append(current_node.val)  # 把该节点的值加入结果集
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
    return  res

if __name__ == '__main__':
    """
          1
         /  \
       2      3
     /  \    /  \
    4    5  6    
    """
    # [1,2,3,4,5,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(bfs(root))


