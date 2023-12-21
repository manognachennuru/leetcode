# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        
        def dfs(node, curSum, curPath):
            
            if not node:
                return 
        
            curSum += node.val
            if not node.left and not node.right: #leaf node
                if curSum == targetSum:
                    paths.append(curPath + [node.val])
                    return
            else:
                #check further
                dfs(node.left, curSum, curPath + [node.val])
                dfs(node.right, curSum, curPath + [node.val])
                
        dfs(root, 0, [])
        return paths
                