# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def balance(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = balance(left, mid - 1)
            node.right = balance(mid + 1, right)
            return node

        # Construct balanced BST from sorted values
        return balance(0, len(nums) - 1)
