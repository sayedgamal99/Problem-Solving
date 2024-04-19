# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height-right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
