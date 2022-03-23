# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        return self.helper(root,key)
    
    def find_min(self,root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root.val
        
    def helper(self,root,key):
        if key < root.val:
            if root.left:
                root.left = self.helper(root.left,key)

        elif key > root.val:
            if root.right:
                root.right = self.helper(root.right,key)

        else:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                min_val = self.find_min(root.right)
                root.val = min_val
                root.right = self.helper(root.right,min_val)
        return root
        
            
        
            