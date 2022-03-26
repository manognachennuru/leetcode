# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        
        if root == None:
            return None
        
        #visit left sub-tree
        if root.left:
            elements += self.inorderTraversal(root.left)

        #visit base node
        elements.append(root.val)
        
        #visit right sub-tree
        if root.right:
            elements += self.inorderTraversal(root.right)
            
        return elements
    