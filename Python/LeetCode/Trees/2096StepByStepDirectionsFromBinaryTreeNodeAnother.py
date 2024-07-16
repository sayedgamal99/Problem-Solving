class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        val = val
        left = left
        right = right


class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        def dfs(node, path, target):
            if not node:
                return ''
            if node.val == target:
                return path
            path.append("L")
            ans = dfs(node.left, path, target)
            if ans:
                return ans
            path.pop()
            path.append('R')
            ans = dfs(node.right, path, target)
            if ans:
                return ans
            path.pop()
            return ''

        startPath = dfs(root, [], startValue)
        destPath = dfs(root, [], destValue)

        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1

        return 'U' * (len(startPath) - i) + ''.join(destPath[i:])
