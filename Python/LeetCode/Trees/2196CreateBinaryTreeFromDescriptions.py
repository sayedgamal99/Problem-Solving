class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        nodes = {}  # Dictionary to store the node values and corresponding TreeNode instances
        children = set()  # Set to keep track of all children nodes

        for parent, child, isleft in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isleft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        # The root node is the one that is not anyone's child
        root_val = (set(nodes.keys()) - children).pop()
        return nodes[root_val]


print(Solution().createBinaryTree(descriptions=[
      [20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]))
