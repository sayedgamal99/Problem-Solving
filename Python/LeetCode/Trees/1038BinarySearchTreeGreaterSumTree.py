# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curSum = 0

        def dfs(node):
            if not node:
                return
            nonlocal curSum
            dfs(node.right)
            node.val += curSum
            curSum = node.val
            dfs(node.left)
        dfs(root)
        return root

    """def bstToGst(self, root: TreeNode) -> TreeNode: # another solution without global curSum (same logic)
        def dfs(node, acc):
                if not node:
                    return acc
                node.val += dfs(node.right, acc)
                return dfs(node.left, node.val)

            dfs(root,0)
            return root"""
