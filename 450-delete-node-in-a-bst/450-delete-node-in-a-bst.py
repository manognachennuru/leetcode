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
        
        if key < root.val:
            if root.left:
                root.left = self.deleteNode(root.left,key)

        elif key > root.val:
            if root.right:
                root.right = self.deleteNode(root.right,key)

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
                root.right = self.deleteNode(root.right,min_val)
        return root  
    
    def find_min(self,root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root.val
        
        
            