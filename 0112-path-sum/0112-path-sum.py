# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #dfs and check values
        
        def dfs(node, target, flag):
            if flag == True:
                return True
            if node: 
                target -= node.val
                if target == 0 and node.left == None and node.right == None:
                    flag = True
                    return flag
                else:
                    return dfs(node.left, target, flag) | dfs(node.right, target, flag)   
            else:
                return False
        
        flag = False
        return dfs(root, targetSum, flag)
        
        
                
            