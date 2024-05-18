# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(cur):
            if not cur:
                return [0, 0]  # [size, coins]
            l_size, l_coins = dfs(cur.left)
            r_size, r_coins = dfs(cur.right)

            size = 1 + l_size + r_size
            coins = cur.val + l_coins + r_coins

            self.res += abs(size - coins)
            return [size, coins]
        dfs(root)
        return self.res


# optimized solution to work with only one variable : extra coins
class Solution2:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(cur):
            if not cur:
                return 0  # extra coins
            l_coins = dfs(cur.left)
            r_coins = dfs(cur.right)

            extra_coins = cur.val - 1 + l_coins + r_coins

            self.res += abs(extra_coins)
            return extra_coins
        dfs(root)
        return self.res
