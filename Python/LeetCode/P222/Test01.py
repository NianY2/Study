"""
222. 完全二叉树的节点个数
https://leetcode.cn/problems/count-complete-tree-nodes/?envType=problem-list-v2&envId=binary-search

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root:Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return  0
        ans = []
        q = [root]
        while q:
            current_node = q.pop(0)
            ans.append(root.val)
            if current_node.left:q.append(current_node.left)
            if current_node.right:q.append(current_node.right)
        return len(ans)



if __name__ == '__main__':
    # [1,2,3,4,5,6]  6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    print(Solution().countNodes(root))
    # [1]  1
    root = TreeNode(1)
    print(Solution().countNodes(root))
    # []  0
    print(Solution().countNodes(None))