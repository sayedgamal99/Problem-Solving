# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root, val: int, depth: int):

        def dfs(node, curr):
            if node is None:
                return None
            if curr == depth-1:
                lTemp = node.left
                rTemp = node.right

                node.left = TreeNode(val, left=lTemp)
                node.right = TreeNode(val, right=rTemp)

                return node

            node.left = dfs(node.left, curr+1)
            node.right = dfs(node.right, curr+1)

            return node

        if depth == 1:
            newTr = TreeNode(val, left=root)
            return newTr

        return dfs(root, 1)
