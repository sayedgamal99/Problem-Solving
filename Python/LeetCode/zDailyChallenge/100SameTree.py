# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution one (hack :))
class Solution:
    def isSameTree(self, p, q) -> bool:
        return str(p) == str(q)
# solution 2
class Solution:
    def isSameTree(self,p,q) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
