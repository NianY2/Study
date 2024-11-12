"""
深度优先搜索（DFS） Deep First Search
"""
from typing import List
from typing_extensions import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root:Optional[TreeNode]) -> List:
    res = []
    q = [root]

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

    print(dfs(root))


