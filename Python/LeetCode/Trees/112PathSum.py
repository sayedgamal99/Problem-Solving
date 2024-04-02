# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, currentS):
            if not root:
                return False

            currentS += root.val
            if not root.left and not root.right:
                return currentS == targetSum

            return (dfs(root.left, currentS) or dfs(root.right, currentS))

        return dfs(root, 0)
