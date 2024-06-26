class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and collect values
        def in_order_traversal(node, values):
            if not node:
                return
            in_order_traversal(node.left, values)
            values.append(node.val)
            in_order_traversal(node.right, values)

        # Helper function to construct a balanced BST from sorted values
        def balance(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_values[mid])
            node.left = balance(left, mid - 1)
            node.right = balance(mid + 1, right)
            return node

        # Perform in-order traversal to get sorted values
        sorted_values = []
        in_order_traversal(root, sorted_values)

        # Construct balanced BST from sorted values
        return balance(0, len(sorted_values) - 1)
