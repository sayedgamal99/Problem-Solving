# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:

        def is_leaf(i,r):
            return ((i*2)+1)<len(r) and r[(i*2)+1]!='null'
        
        theleafs = []
        for i in range(len(root1)):
            if is_leaf(i,root1):
                theleafs.append(root1[i])
                
        theleafs2=[]
        for j in range(len(root2)):
            if is_leaf(j,root2):
                theleafs2.append(root2[j])
        
        return theleafs==theleafs2
    
# print(Solution().leafSimilar(root1 = [3, 5,1,6,2,9,8,'null','null',7,4], root2 = [3,5,1,6,7,4,2,'null','null','null','null','null','null',9,8]))
    

def generate_numbers(n):
    for i in range(n):
        yield i


# Using the generator
my_generator = generate_numbers(5)

for number in my_generator:
    print(number)
