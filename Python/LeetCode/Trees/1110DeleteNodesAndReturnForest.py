# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete = set(to_delete)
        forest = [] if root.val in to_delete else [root]

        def dfs(node, parent, isLeft):
            if node is None:
                return
            dfs(node.left, node, True)
            dfs(node.right, node, False)
            if node.val in to_delete:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                if parent:
                    if isLeft:
                        parent.left = None
                    else:
                        parent.right = None
        dfs(root, None, False)
        return forest
