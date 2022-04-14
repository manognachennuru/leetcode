# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft = False) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None and isLeft == True:
            return root.val
        
        sm = 0
        
        #check for subtrees
        if root.left:
            sm += self.sumOfLeftLeaves(root.left,True)
        if root.right:
            sm += self.sumOfLeftLeaves(root.right,False)
        
        return sm
    
    