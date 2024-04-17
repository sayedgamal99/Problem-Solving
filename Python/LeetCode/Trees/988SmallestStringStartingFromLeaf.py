class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, current):
            if not node:
                return ''
            current += chr(node.val + ord('a'))
            if not node.left and not node.right:
                return current[::-1]
            left_path = dfs(node.left, current)
            right_path = dfs(node.right, current)
            return min(filter(None, (left_path, right_path)))

        return dfs(root, '')


def run_tests():
    solution = Solution()

    # Test Case 1
    #        0
    #       / \
    #      1   2
    #     /|   |\
    #    3 4   3 4
    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(4)

    output = solution.smallestFromLeaf(root1)
    try:
        assert output == "dba"
        print("All test cases passed!")
    except:
        print("Wrong Answer: ", output)


run_tests()
