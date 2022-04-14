# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        sm = 0
        if root.left != None: 
            #left node exists, check if it is a leaf node
            if root.left.left == None and root.left.right == None:
                sm += root.left.val
        
        #check for subtrees
        sm += self.sumOfLeftLeaves(root.left)
        sm += self.sumOfLeftLeaves(root.right)
        
        return sm
    
    