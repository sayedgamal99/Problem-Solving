# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        pass


def run_tests():
    solution = Solution()

    # Test Case 1
    #   3
    #  / \
    # 9  20
    #   /  \
    #  15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution.sumOfLeftLeaves(root1) == 24

    print("All test cases passed!")


run_tests()
