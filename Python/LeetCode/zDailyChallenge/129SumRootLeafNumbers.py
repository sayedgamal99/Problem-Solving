class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:
        def dfs(node, current_path):
            if not node:
                return 0
            current_path = current_path*10 + node.val
            if (not node.left) and (not node.right):  # leaf node (base case)
                return current_path
            return dfs(node.left, current_path) + dfs(node.right, current_path)

        return dfs(root, 0)


def run_tests():
    solution = Solution()

    # Test Case 1
    #   4
    #  / \
    # 0  9
    #   /  \
    #   5   1
    root1 = TreeNode(4)
    root1.left = TreeNode(0)
    root1.right = TreeNode(9)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(1)
    try:
        assert solution.sumNumbers(root1) == 1026
        print("All test cases passed!")
    except AssertionError:
        print('Wrong Answer: ', solution.sumNumbers(root1))


run_tests()
